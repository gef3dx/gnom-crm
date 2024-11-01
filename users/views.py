from django.contrib import messages
from django.utils import timezone
import asyncio
from django.contrib.auth.views import LoginView as Login
from aiogram import Bot, types
from aiogram.enums.parse_mode import ParseMode
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

API_TOKEN = '6948387483:AAGPQoV5YQ_utPygbXvuCir0RXSDH79vw0w'
CHAT_ID = '-1001998408167'


def create_bot():
    return Bot(token=API_TOKEN)


async def send_login_info(user_email, login_time):
    bot = create_bot()
    message = f"Пользователь с email: {user_email} вошел в систему в {login_time}."
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=ParseMode.HTML)
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")
    finally:
        await bot.session.close()


def send_login_info_sync(user_email, login_time):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(send_login_info(user_email, login_time))
    loop.close()


class LoginView(Login):
    template_name = "users/login.html"
    redirect_authenticated_user = True
    extra_context = {
        "title": "Авторизация"
    }

    def form_valid(self, form):
        user = form.get_user()
        login_time = str(datetime.now())[:19]

        # Отправка сообщения в Telegram в отдельном потоке
        with ThreadPoolExecutor() as executor:
            executor.submit(send_login_info_sync, user.email, login_time)

        messages.success(self.request, f"Добро пожаловать, {user.email}!")
        return super().form_valid(form)
