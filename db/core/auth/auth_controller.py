from aiogram import types
from aiogram.types import InlineKeyboardButton, WebAppInfo, InlineKeyboardMarkup

from core.auth.auth_service import check_user_registration, register_user
from aiogram.filters import CommandStart

def register_handlers(session, dp):
    """
    Регистрация всех обработчиков для авторизации.
    """
    print("kjkjhjhk")
    @dp.message(CommandStart())
    async def start_handler(message: types.Message):
        user_id = message.from_user.id
        user_name = message.from_user.username or message.from_user.first_name
        print("ettttt")
        web_app_button = InlineKeyboardButton(
            text="Open Web App",
            web_app=WebAppInfo(url="https://timofeirazow.github.io/decetration-tot/")  # Замените на ваш URL веб-приложения
        )

    # Создаем разметку клавиатуры с кнопкой
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[web_app_button]])
        # Проверяем, зарегистрирован ли пользователь
        is_registered = check_user_registration(session, user_id)

        if is_registered:
            await message.answer(f"Добро пожаловать, {user_name}! Вы уже зарегистрированы.", reply_markup=keyboard)
        else:
            # Регистрация нового пользователя
            register_user(session, user_id, user_name)
            await message.answer(f"Привет, {user_name}! Вы успешно зарегистрированы!", reply_markup=keyboard)
