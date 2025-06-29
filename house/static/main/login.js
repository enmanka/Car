document.addEventListener('DOMContentLoaded', () => {
    let isLogin = true;
    const formTitle = document.getElementById('form-title');
    const submitBtn = document.getElementById('submit-btn');
    const toggleMode = document.getElementById('toggle-mode');
    const errorMsg = document.getElementById('error-message');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');

    // 初始化SVG动画效果
    initSVGAnimations();

    toggleMode.addEventListener('click', (e) => {
        e.preventDefault();
        isLogin = !isLogin;
        submitBtn.textContent = isLogin ? '登录' : '注册';
        toggleMode.textContent = isLogin ? '切换到注册' : '切换到登录';
        errorMsg.textContent = '';
    });

    submitBtn.addEventListener('click', async () => {
        const username = usernameInput.value.trim();
        const password = passwordInput.value.trim();

        if (!username || !password) {
            errorMsg.textContent = '用户名和密码不能为空';
            return;
        }

        const endpoint = isLogin ? '/data/login' : '/data/register';

        try {
            submitBtn.disabled = true;
            submitBtn.textContent = '处理中...';

            const response = await fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    usr_name: username,
                    pwd: password
                })
            });

            submitBtn.disabled = false;
            submitBtn.textContent = isLogin ? '登录' : '注册';

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || '请求失败');
            }

            const data = await response.json();

            if (isLogin) {
                localStorage.setItem('authToken', data.token);
                window.location.href = '../static/main.html';
            } else {
                isLogin = true;
                submitBtn.textContent = '登录';
                toggleMode.textContent = '切换到注册';
                errorMsg.textContent = '注册成功！请登录';
                usernameInput.value = '';
                passwordInput.value = '';
            }
        } catch (err) {
            errorMsg.textContent = err.message.includes('<') ?
                '服务器错误，请稍后再试' :
                err.message;
            submitBtn.disabled = false;
            submitBtn.textContent = isLogin ? '登录' : '注册';
        }
    });

    function initSVGAnimations() {
        const eyeLeft = document.querySelector('.eyeL');
        const eyeRight = document.querySelector('.eyeR');
        const nose = document.querySelector('.nose');
        const mouth = document.querySelector('.mouth');
        const face = document.querySelector('.face');
        const armLeft = document.querySelector('.armL');
        const armRight = document.querySelector('.armR');

        // 默认隐藏手臂
        armLeft.style.opacity = '0';
        armRight.style.opacity = '0';

        // 密码输入时显示手臂（遮眼动画）
        passwordInput.addEventListener('focus', () => {
            armLeft.style.opacity = '1';
            armRight.style.opacity = '1';
            armLeft.style.transform = 'translateX(-93px) translateY(2px)';
            armRight.style.transform = 'translateX(-93px) translateY(2px)';
        });

        passwordInput.addEventListener('blur', () => {
            // 恢复隐藏状态
            armLeft.style.opacity = '0';
            armRight.style.opacity = '0';
            armLeft.style.transform = '';
            armRight.style.transform = '';
        });
        // 鼠标移动控制眼睛跟随
        document.addEventListener('mousemove', (event) => {
            const x = (event.clientX * 100) / window.innerWidth;
            const y = (event.clientY * 100) / window.innerHeight;

            const offsetX = (x - 50) / 10;
            const offsetY = (y - 50) / 10;

            if (eyeLeft) eyeLeft.style.transform = `translate(${offsetX}px, ${offsetY}px)`;
            if (eyeRight) eyeRight.style.transform = `translate(${offsetX}px, ${offsetY}px)`;
            if (nose) nose.style.transform = `translate(${offsetX / 2}px, ${offsetY / 2}px)`;
            if (mouth) mouth.style.transform = `translate(${offsetX / 2}px, ${offsetY / 2}px)`;
            if (face) face.style.transform = `translate(${offsetX / 3}px, ${offsetY / 3}px)`;
        });

        // 输入框交互控制嘴巴动画
        usernameInput.addEventListener('focus', () => {
            if (mouth) {
                mouth.setAttribute('d', 'M15,20 C20,25 30,25 35,20'); // 微笑
            }
        });

        usernameInput.addEventListener('blur', () => {
            if (mouth) {
                mouth.setAttribute('d', 'M15,25 C20,20 30,20 35,25'); // 原始
            }
        });

        passwordInput.addEventListener('focus', () => {
            if (mouth) {
                mouth.setAttribute('d', 'M15,30 C20,35 30,35 35,30'); // 嚼牙
            }
        });

        passwordInput.addEventListener('blur', () => {
            if (mouth) {
                mouth.setAttribute('d', 'M15,25 C20,20 30,20 35,25'); // 恢复
            }
        });
    }
});