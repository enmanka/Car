// 获取当前用户
const username = localStorage.getItem('username');
// 全局变量存储当前要删除的评论ID
let currentDeleteCommentId = null;

if (username) {
    document.getElementById('profileName').textContent = username;
} else {
    document.getElementById('profileName').textContent = "未登录";
    window.location.href = "/";
}

const avatarIndex = localStorage.getItem('avatarIndex') || '1';
document.getElementById('userAvatar').src = `../static/img/${avatarIndex}.jpg`;

// 加载用户评论
function loadUserComments() {
    if (!username) {
        document.querySelector('#reviews .content-box').innerHTML = '<p>请先登录查看评论</p>';
        return;
    }

    fetch(`/api/comment/my_comments?username=${username}`)
        .then(response => {
            if (!response.ok) throw new Error('获取评论失败');
            return response.json();
        })
        .then(comments => {
            renderComments(comments);
        })
        .catch(error => {
            console.error('加载评论失败:', error);
            document.querySelector('#reviews .content-box').innerHTML =
                `<p style="color:#ff6b6b;">加载失败: ${error.message}</p>`;
        });
}

// 渲染评论列表
function renderComments(comments) {
    const container = document.querySelector('#reviews .content-box');

    if (!comments || comments.length === 0) {
        container.innerHTML = '<p>暂无评价数据。</p>';
        return;
    }

    let html = '';
    comments.forEach(comment => {
        html += `
            <div style="margin-bottom: 15px; padding: 15px; background: #3a3a50; border-radius: 8px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                    <strong class="car-name-delete" data-id="${comment.id}" 
                            style="color: #66fcf1; cursor: pointer; text-decoration: underline;">
                        ${comment.car_name || '未知车型'}
                    </strong>
                    <span style="color: #888; font-size: 0.9rem;">${formatDateTime(comment.created_at)}</span>
                </div>
                <p style="margin: 0 0 8px; color: #f1f1f1;">${comment.content || '无内容'}</p>
                <div style="color: #888; font-size: 0.9rem;">
                    <i class="ri-heart-fill" style="color: #ff4757;"></i> ${comment.like_count || 0} 点赞
                </div>
            </div>
        `;
    });

    container.innerHTML = html;
}

// 显示删除确认弹窗
function showDeleteModal(commentId) {
    currentDeleteCommentId = commentId;
    document.getElementById('deleteModal').style.display = 'flex';
}

// 隐藏删除确认弹窗
function hideDeleteModal() {
    document.getElementById('deleteModal').style.display = 'none';
}

// 确认删除评论
// 确认删除评论
function confirmDelete() {
    if (!currentDeleteCommentId) return;

    const username = localStorage.getItem('username');
    if (!username) {
        alert('请先登录');
        return;
    }

    // 添加加载状态
    const deleteBtn = document.getElementById('confirmDelete');
    const originalText = deleteBtn.textContent;
    deleteBtn.disabled = true;
    deleteBtn.innerHTML = '<i class="ri-loader-4-line spin"></i> 删除中...';

    fetch(`/api/comment/${currentDeleteCommentId}?username=${username}`, {
        method: 'DELETE',
        headers: {
            'Accept': 'application/json',
        }
    })
        .then(async response => {
            const data = await response.json();
            if (!response.ok) {
                throw new Error(data.error || '删除失败');
            }
            return data;
        })
        .then(data => {
            hideDeleteModal();
            loadUserComments();
            alert(data.message || '删除成功');
        })
        .catch(error => {
            console.error('删除评论失败:', error);
            alert('删除失败: ' + error.message);
        })
        .finally(() => {
            deleteBtn.disabled = false;
            deleteBtn.textContent = originalText;
        });
}

// 格式化日期时间
function formatDateTime(dateString) {
    if (!dateString) return '未知时间';
    const date = new Date(dateString);
    const Y = date.getFullYear();
    const M = String(date.getMonth() + 1).padStart(2, '0');
    const D = String(date.getDate()).padStart(2, '0');
    const h = String(date.getHours()).padStart(2, '0');
    const m = String(date.getMinutes()).padStart(2, '0');
    return `${Y}-${M}-${D} ${h}:${m}`;
}

// 标签切换函数
function switchTab(tabId) {
    // 移除所有active类
    document.querySelectorAll('.nav-tab').forEach(tab => tab.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));

    // 添加active类到当前标签
    document.querySelector(`.nav-tab[onclick*="${tabId}"]`).classList.add('active');
    document.getElementById(tabId).classList.add('active');

    // 如果是评论标签则加载数据
    if (tabId === 'reviews') {
        loadUserComments();
    }
}

// 初始化删除弹窗事件和评论点击事件
function initEventListeners() {
    document.getElementById('confirmDelete').addEventListener('click', confirmDelete);
    document.getElementById('cancelDelete').addEventListener('click', hideDeleteModal);

    // 点击弹窗外部关闭
    document.getElementById('deleteModal').addEventListener('click', (e) => {
        if (e.target === document.getElementById('deleteModal')) {
            hideDeleteModal();
        }
    });

    // 使用事件委托处理评论点击
    document.querySelector('#reviews .content-box').addEventListener('click', (e) => {
        if (e.target.classList.contains('car-name-delete') || e.target.closest('.car-name-delete')) {
            const commentElement = e.target.classList.contains('car-name-delete')
                ? e.target
                : e.target.closest('.car-name-delete');
            const commentId = commentElement.dataset.id;
            showDeleteModal(commentId);
        }
    });
}

// 页面加载时初始化
document.addEventListener('DOMContentLoaded', () => {
    // 头像选择功能
    const avatarImg = document.getElementById('userAvatar');
    const avatarModal = document.getElementById('avatarModal');
    const avatarList = document.getElementById('avatarList');

    const totalAvatars = 8;
    for (let i = 1; i <= totalAvatars; i++) {
        const img = document.createElement('img');
        img.src = `../static/img/${i}.jpg`;
        img.alt = `头像${i}`;
        img.style.width = '60px';
        img.style.cursor = 'pointer';
        img.style.borderRadius = '50%';

        img.addEventListener('click', async () => {
            avatarImg.src = `../static/img/${i}.jpg`;
            avatarModal.style.display = 'none';
            localStorage.setItem('avatarIndex', i);
        });

        avatarList.appendChild(img);
    }

    avatarImg.addEventListener('click', (e) => {
        e.stopPropagation();
        avatarModal.style.display = avatarModal.style.display === 'none' ? 'block' : 'none';
        avatarModal.style.top = `${e.clientY + 10}px`;
        avatarModal.style.left = `${e.clientX}px`;
    });

    document.addEventListener('click', () => {
        avatarModal.style.display = 'none';
    });

    // 初始化事件监听器
    initEventListeners();

    // 初始化加载下载记录和用户评论
    loadDownloadRecords();
    loadUserComments();
});

// 加载下载记录
function loadDownloadRecords() {
    if (!username) {
        document.getElementById('download-list').innerHTML = '<li>未登录，无法获取下载记录。</li>';
        return;
    }

    fetch(`/data/getExportRecords?user_name=${encodeURIComponent(username)}`)
        .then(res => {
            if (!res.ok) throw new Error('网络请求失败');
            return res.json();
        })
        .then(data => {
            const list = document.getElementById('download-list');
            if (!data.length) {
                list.innerHTML = '<li>暂无下载记录。</li>';
                return;
            }
            data.sort((a, b) => new Date(b.export_time) - new Date(a.export_time));

            list.innerHTML = data.map(item => `
                <li style="padding:10px 0; border-bottom:1px solid #555; display:flex; justify-content:space-between; font-size:14px;">
                    <span style="color:#66fcf1;">${formatDateTime(item.export_time)}</span>
                    <span title="${item.csv_filename}" style="max-width:60%; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${item.csv_filename}</span>
                </li>
            `).join('');
        })
        .catch(err => {
            document.getElementById('download-list').innerHTML = `<li>加载失败：${err.message}</li>`;
        });
}

// 退出登录
document.getElementById("logoutBtn").onclick = function () {
    localStorage.clear();
    sessionStorage.clear();
    document.cookie.split(";").forEach(function (c) {
        document.cookie = c.replace(/^ +/, "").replace(/=.*/, "=;expires=" + new Date().toUTCString() + ";path=/");
    });
    window.location.href = "/";
};

// 修改密码
document.addEventListener('DOMContentLoaded', () => {
    const changeBtn = document.getElementById('change-btn');
    const changeMsg = document.getElementById('change-message');

    changeBtn.addEventListener('click', async () => {
        const oldPwd = document.getElementById('old-password').value.trim();
        const newPwd = document.getElementById('new-password').value.trim();
        const confirmPwd = document.getElementById('confirm-password').value.trim();

        if (!oldPwd || !newPwd || !confirmPwd) {
            changeMsg.style.color = 'red';
            changeMsg.textContent = '请填写完整信息';
            return;
        }

        if (newPwd !== confirmPwd) {
            changeMsg.style.color = 'red';
            changeMsg.textContent = '两次输入的新密码不一致';
            return;
        }

        try {
            changeBtn.disabled = true;
            changeBtn.textContent = '处理中...';

            const response = await fetch('/data/change_password', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${localStorage.getItem('authToken')}`
                },
                body: JSON.stringify({
                    usr_name: username,
                    old_pwd: oldPwd,
                    new_pwd: newPwd
                })
            });

            if (!response.ok) throw new Error('修改失败');

            changeMsg.style.color = 'green';
            changeMsg.textContent = '密码修改成功';
            document.getElementById('old-password').value = '';
            document.getElementById('new-password').value = '';
            document.getElementById('confirm-password').value = '';
        } catch (err) {
            changeMsg.style.color = 'red';
            changeMsg.textContent = err.message;
        } finally {
            changeBtn.disabled = false;
            changeBtn.textContent = '提交修改';
        }
    });
});

// AI车型推荐
async function getCarRecommendation() {
    const budget = document.getElementById('budget').value;
    const purpose = document.getElementById('purpose').value;
    const requirements = document.getElementById('requirements').value;

    const resultDiv = document.getElementById('recommendation-result');
    const contentDiv = document.getElementById('recommendation-content');
    resultDiv.style.display = 'block';
    contentDiv.innerHTML = '<p><i class="ri-loader-4-line spin"></i> AI正在思考...</p>';

    try {
        const response = await fetch('https://api.deepseek.com/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer sk-bb676e8c4a0a4263a0ad340ecc7274cd'
            },
            body: JSON.stringify({
                model: "deepseek-chat",
                messages: [{
                    role: "user",
                    content: `请推荐3款适合预算${budget}万元、主要用途为${purpose}的车型。${requirements ? '其他需求：' + requirements : ''}。要求：1.包含品牌、型号、价格 2.简短推荐理由 3.用中文回答`
                }],
                temperature: 0.7,
                max_tokens: 500
            })
        });
        const data = await response.json();
        contentDiv.innerHTML = markdownToHtml(data.choices[0].message.content);
    } catch (error) {
        contentDiv.innerHTML = `<p style="color:#ff6b6b;">请求失败: ${error.message}</p>`;
    }
}

function markdownToHtml(md) {
    return md
        .replace(/^### (.*$)/gm, '<h4>$1</h4>')
        .replace(/^## (.*$)/gm, '<h3>$1</h3>')
        .replace(/^# (.*$)/gm, '<h2>$1</h2>')
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(.*?)\*/g, '<em>$1</em>')
        .replace(/\n/g, '<br>');
}

// 添加旋转动画样式
const style = document.createElement('style');
style.textContent = `
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    .spin {
        animation: spin 1s linear infinite;
        display: inline-block;
    }
`;
document.head.appendChild(style);