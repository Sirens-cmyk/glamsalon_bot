<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>سالن زیبایی نیکان</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>

    <style>
        /* تعریف فونت و رنگ‌های جدید شبیه عکس */
        :root {
            --pink-gradient: linear-gradient(180deg, #ff85a1 0%, #ff477e 100%);
            --glass-bg: rgba(255, 255, 255, 0.25);
            --text-color: #ffffff;
        }

        body {
            font-family: 'Tahoma', sans-serif;
            /* عکس پس‌زمینه اکلیلی و صورتی */
            background: url('https://img.freepik.com/free-vector/glittery-pink-bokeh-background-design_53876-101150.jpg') no-repeat center center fixed;
            background-size: cover;
            color: var(--text-color);
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }

        .header {
            text-align: center;
            margin-bottom: 20px;
            background: var(--glass-bg);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            padding: 20px;
            border-radius: 25px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            width: 90%;
            max-width: 400px;
        }

        .header h1 {
            margin: 0;
            font-size: 24px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }

        .service-card {
            background: var(--glass-bg);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border-radius: 20px;
            padding: 15px;
            width: 100%;
            max-width: 380px;
            margin-bottom: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s ease;
            cursor: pointer;
            box-sizing: border-box;
        }

        .service-card:hover {
            transform: translateY(-3px);
            background: rgba(255, 255, 255, 0.35);
        }

        .service-card.selected {
            border: 2px solid #ffffff;
            background: rgba(255, 255, 255, 0.4);
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.5);
        }

        .service-info h3 {
            margin: 0 0 5px 0;
            font-size: 16px;
        }

        .service-info p {
            margin: 0;
            font-size: 12px;
            opacity: 0.9;
        }

        .price {
            font-weight: bold;
            background: rgba(255, 255, 255, 0.2);
            padding: 5px 10px;
            border-radius: 12px;
        }

        .main-button {
            background: var(--pink-gradient);
            color: white;
            border: none;
            padding: 18px;
            border-radius: 50px;
            font-size: 18px;
            font-weight: bold;
            width: 100%;
            max-width: 380px;
            margin-top: auto;
            margin-bottom: 20px;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(255, 71, 126, 0.4);
            transition: 0.3s;
            text-shadow: 0 1px 2px rgba(0,0,0,0.2);
        }

        .main-button:active {
            transform: scale(0.98);
        }

        #services {
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
    </style>
</head>
<body>

    <div class="header">
        <div style="font-size: 40px; margin-bottom: 10px;">🌸</div>
        <h1>سالن زیبایی نیکان</h1>
        <p>رزرو آنلاین نوبت</p>
    </div>

    <div id="services">
        </div>

    <button class="main-button" onclick="sendData()">شروع رزرو نوبت</button>

    <script>
        const tg = window.Telegram.WebApp;
        tg.expand();
        tg.MainButton.hide(); // استفاده از دکمه طراحی شده خودمان

        let selected = null;

        // شبیه‌سازی لود خدمات (اگر فایل JSON داری)
        fetch("services.json")
            .then(res => res.json())
            .then(data => renderServices(data))
            .catch(() => {
                // اگر فایل نبود، چند دیتای تستی نشون بده
                const fallbackData = [
                    {name: "میکاپ تخصصی", description: "شامل کانتورینگ و مژه", price: "۲,۰۰۰,۰۰۰ ت"},
                    {name: "کاشت ناخن", description: "پودر و ژل با طراحی", price: "۴۵۰,۰۰۰ ت"},
                    {name: "کوتاهی مو", description: "ژورنالی و ساده", price: "۳۰۰,۰۰۰ ت"}
                ];
                renderServices(fallbackData);
            });

        function renderServices(services) {
            const container = document.getElementById("services");
            container.innerHTML = "";

            services.forEach(service => {
                const card = document.createElement("div");
                card.className = "service-card";
                card.onclick = () => selectService(card, service);

                card.innerHTML = `
                    <div class="service-info">
                        <h3>${service.name}</h3>
                        <p>${service.description}</p>
                    </div>
                    <div class="price">${service.price}</div>
                `;

                container.appendChild(card);
            });
        }

        function selectService(element, service) {
            document.querySelectorAll('.service-card')
                .forEach(card => card.classList.remove('selected'));

            element.classList.add('selected');
            selected = service;
        }

        function sendData() {
            if (!selected) {
                tg.showAlert("لطفاً ابتدا یک خدمت را انتخاب کنید 🌸");
                return;
            }

            tg.sendData(JSON.stringify(selected));
            tg.close();
        }
    </script>
</body>
</html>
