// 获取URL中的username、password、图片参数
//const urlParams = new URLSearchParams(window.location.search);
const username = localStorage.getItem('username');
if (username) {
    document.getElementById('profileName').textContent = username;
} else {
    document.getElementById('profileName').textContent = "未登录";
    window.location.href = "/";
}
const avatarIndex = localStorage.getItem('avatarIndex') || '1';  // 默认1
document.getElementById('userAvatar').src = `../static/img/${avatarIndex}.jpg`;

function loadDownloadRecords() {
    if (!username) {
        document.getElementById('download-list').innerHTML = '<li>未登录，无法获取下载记录。</li>';
        return;
    }

    // 这里直接用 username 请求接口，不用再从外面传参数
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

document.addEventListener('DOMContentLoaded', () => {
    const avatarImg = document.getElementById('userAvatar');
    const avatarModal = document.getElementById('avatarModal');
    const avatarList = document.getElementById('avatarList');

    const token = localStorage.getItem('authToken');
    const username = localStorage.getItem('username');

    // 加载头像列表
    const totalAvatars = 5;
    for (let i = 1; i <= totalAvatars; i++) {
        const img = document.createElement('img');
        img.src = `../static/img/${i}.jpg`;
        img.alt = `头像${i}`;
        img.style.width = '60px';
        img.style.cursor = 'pointer';
        img.style.borderRadius = '50%';

        img.addEventListener('click', async () => {
            avatarImg.src = `../static/img/${i}.jpg`;  // 修改头像显示
            avatarModal.style.display = 'none';        // 关闭弹窗

            // 提交头像编号到后端
            try {
                const res = await fetch('/data/update_avatar', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${token}`
                    },
                    body: JSON.stringify({
                        usr_name: username,
                        avatar_index: i
                    })
                });

                const result = await res.json();
                if (!res.ok) {
                    throw new Error(result.error || '头像修改失败');
                }
                else {
                    localStorage.setItem('avatarIndex', i);
                }
            } catch (err) {
                alert('头像修改失败：' + err.message);
            }
        });

        avatarList.appendChild(img);
        loadDownloadRecords();
    }

    // 点击头像显示/隐藏弹窗
    avatarImg.addEventListener('click', (e) => {
        avatarModal.style.display = avatarModal.style.display === 'none' ? 'block' : 'none';
        avatarModal.style.top = `${e.clientY + 10}px`;
        avatarModal.style.left = `${e.clientX}px`;
    });

    // 点击外部关闭弹窗
    document.addEventListener('click', (e) => {
        if (!avatarModal.contains(e.target) && e.target !== avatarImg) {
            avatarModal.style.display = 'none';
        }
    });
});

function formatDateTime(dateStr) {
    const date = new Date(dateStr);
    // 格式化成 "YYYY-MM-DD HH:mm:ss" 或其他你想要的格式
    const Y = date.getFullYear();
    const M = String(date.getMonth() + 1).padStart(2, '0');
    const D = String(date.getDate()).padStart(2, '0');
    const h = String(date.getHours()).padStart(2, '0');
    const m = String(date.getMinutes()).padStart(2, '0');
    const s = String(date.getSeconds()).padStart(2, '0');
    return `${Y}-${M}-${D} ${h}:${m}:${s}`;
}

document.getElementById("logoutBtn").onclick = function () {
    // 清除 localStorage 和 sessionStorage
    localStorage.clear();
    sessionStorage.clear();

    // 清除所有 cookie
    document.cookie.split(";").forEach(function (c) {
        document.cookie = c
            .replace(/^ +/, "")
            .replace(/=.*/, "=;expires=" + new Date().toUTCString() + ";path=/");
    });

    // 跳转到登录页面
    window.location.href = "/"; // 请根据你项目路径修改
};

// 标签切换函数
function switchTab(tabId) {
    document.querySelectorAll('.nav-tab').forEach(tab => tab.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));

    document.querySelector(`.nav-tab[onclick*="${tabId}"]`).classList.add('active');
    document.getElementById(tabId).classList.add('active');
}

document.addEventListener('DOMContentLoaded', () => {
    const oldPwdInput = document.getElementById('old-password');
    const newPwdInput = document.getElementById('new-password');
    const confirmPwdInput = document.getElementById('confirm-password');
    const changeBtn = document.getElementById('change-btn');
    const changeMsg = document.getElementById('change-message');

    changeBtn.addEventListener('click', async () => {
        const oldPwd = oldPwdInput.value.trim();
        const newPwd = newPwdInput.value.trim();
        const confirmPwd = confirmPwdInput.value.trim();

        // 检查填写完整性
        if (!oldPwd || !newPwd || !confirmPwd) {
            changeMsg.style.color = 'red';
            changeMsg.textContent = '请填写完整信息';
            return;
        }

        // 检查两次新密码一致性
        if (newPwd !== confirmPwd) {
            changeMsg.style.color = 'red';
            changeMsg.textContent = '两次输入的新密码不一致';
            return;
        }

        try {
            changeBtn.disabled = true;
            changeBtn.textContent = '处理中...';

            const token = localStorage.getItem('authToken');
            const username = localStorage.getItem('username');

            const response = await fetch('/data/change_password', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({
                    usr_name: username,
                    old_pwd: oldPwd,
                    new_pwd: newPwd
                })
            });

            changeBtn.disabled = false;
            changeBtn.textContent = '提交修改';

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || '修改失败');
            }

            changeMsg.style.color = 'green';
            changeMsg.textContent = '密码修改成功';

            // 清空输入
            oldPwdInput.value = '';
            newPwdInput.value = '';
            confirmPwdInput.value = '';

            // setTimeout(() => {
            //     window.location.href = '/'; // 或者跳转至登录页
            // }, 2000);

        } catch (err) {
            changeBtn.disabled = false;
            changeBtn.textContent = '提交修改';
            changeMsg.style.color = 'red';
            changeMsg.textContent = err.message.includes('<') ? '服务器错误' : err.message;
        }
    });
});
