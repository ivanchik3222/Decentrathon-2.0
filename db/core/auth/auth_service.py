from db.db_session import get_user_by_id, create_user

def check_user_registration(session, user_id):
    """
    Проверяет, зарегистрирован ли пользователь в базе данных.
    :param user_id: ID пользователя в Telegram.
    :return: True, если пользователь зарегистрирован, иначе False.
    """
    user = get_user_by_id(session, user_id)
    return user is not None

def register_user(session, user_id, user_name):
    """
    Регистрирует нового пользователя в базе данных.
    :param user_id: ID пользователя в Telegram.
    :param user_name: Имя пользователя в Telegram.
    """
    create_user(session, user_id, user_name)
