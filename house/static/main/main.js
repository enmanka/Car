// 获取用户信息
const username = localStorage.getItem('username');
const avatarIndex = localStorage.getItem('avatarIndex') || '1'; // 默认为1

// 显示用户信息
document.getElementById('usernameDisplay').textContent = username || '访客';
document.getElementById('userAvatar').src = `../static/img/${avatarIndex}.jpg`;

// 导航菜单激活状态
const links = document.querySelectorAll('.nav-link');
links.forEach(link => {
    link.addEventListener('click', function () {
        links.forEach(l => l.classList.remove('active'));
        this.classList.add('active');
    });
});

// 设置主界面入口的链接
document.getElementById('homeEntry').addEventListener('click', function (e) {
    e.preventDefault();
    window.location.href = `../static/home.html`;
});

// 侧边栏折叠功能
const sidebar = document.getElementById('sidebar');
const collapseBtn = document.getElementById('collapseBtn');

collapseBtn.addEventListener('click', () => {
    sidebar.classList.toggle('collapsed');
    updateIcon();
});

function updateIcon() {
    const icon = collapseBtn.querySelector('i');
    icon.className = sidebar.classList.contains('collapsed')
        ? 'ri-arrow-right-s-line'
        : 'ri-arrow-left-s-line';
}

// 新增AI助手交互逻辑
document.getElementById('aiAssistant').addEventListener('click', function () {
    // 清空之前的结果和重置表单
    document.getElementById('ai-result-content').innerHTML = '';
    document.getElementById('aiResult').style.display = 'none';
    document.getElementById('ai-budget').value = 20;
    document.getElementById('ai-budget-value').textContent = 20;
    document.getElementById('ai-purpose').value = "家庭日常使用";
    document.getElementById('ai-requirements').value = "";
    document.getElementById('aiModal').style.display = 'block';
});

document.getElementById('aiModalClose').addEventListener('click', function () {
    document.getElementById('aiModal').style.display = 'none';
});

document.getElementById('aiSubmit').addEventListener('click', function () {
    const budget = document.getElementById('ai-budget').value;
    const purpose = document.getElementById('ai-purpose').value;
    const requirements = document.getElementById('ai-requirements').value;

    // 显示加载状态
    document.getElementById('aiLoading').style.display = 'block';
    document.getElementById('aiResult').style.display = 'none';

    // 调用DeepSeek API
    fetch('https://api.deepseek.com/v1/chat/completions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer sk-bb676e8c4a0a4263a0ad340ecc7274cd' // 替换为你的真实API密钥
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
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('网络响应不正常');
            }
            return response.json();
        })
        .then(data => {
            if (data.choices && data.choices[0] && data.choices[0].message) {
                const recommendation = data.choices[0].message.content;
                document.getElementById('ai-result-content').innerHTML = formatRecommendation(recommendation);
            } else {
                throw new Error('API返回数据格式不正确');
            }
        })
        .catch(error => {
            console.error('API请求失败:', error);
            document.getElementById('ai-result-content').innerHTML =
                `<p style="color:#ff6b6b;">请求失败: ${error.message}</p>
             <p>${getFallbackRecommendation(budget, purpose, requirements)}</p>`;
        })
        .finally(() => {
            document.getElementById('aiLoading').style.display = 'none';
            document.getElementById('aiResult').style.display = 'block';
        });
});

// 格式化API返回的推荐结果
function formatRecommendation(text) {
    // 简单处理Markdown格式
    return text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\n/g, '<br>');
}

// 备用推荐数据（当API不可用时）
function getFallbackRecommendation(budget, purpose, requirements) {
    const recommendations = {
        "家庭日常使用": [
            "1. <strong>丰田卡罗拉</strong> (10-15万): 经济实惠，油耗低，维修成本低",
            "2. <strong>本田思域</strong> (12-18万): 动力充沛，空间适中，保值率高",
            "3. <strong>大众速腾</strong> (13-17万): 德系品质，舒适性好，安全性高"
        ],
        "商务接待": [
            "1. <strong>奔驰E级</strong> (40-60万): 豪华品牌，商务气质，舒适性极佳",
            "2. <strong>奥迪A6L</strong> (35-55万): 官车形象，科技感强，空间宽敞",
            "3. <strong>丰田亚洲龙</strong> (20-30万): 性价比高，混动版本省油"
        ]
        // 可以添加更多场景...
    };

    let result = `<p><strong>基于您的预算(${budget}万)和用途(${purpose})推荐:</strong></p>`;

    if (recommendations[purpose]) {
        result += '<ul>';
        recommendations[purpose].forEach(item => {
            result += `<li>${item}</li>`;
        });
        result += '</ul>';
    } else {
        result += '<p>暂无特定推荐，建议考虑丰田、本田或大众的中端车型。</p>';
    }

    result += '<p style="color:#888;font-size:0.9em;">注：这是本地备用推荐，AI服务可能暂时不可用</p>';
    return result;
}