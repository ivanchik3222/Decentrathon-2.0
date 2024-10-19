from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db.models import Base
from core.auth.auth_models import User

def init_db(database_url):
    """
    Функция для инициализации базы данных, создания таблиц и сессии.

    :param database_url: URL подключения к базе данных (например, "postgresql://user:password@localhost/dbname")
    :return: Сессия для взаимодействия с базой данных
    """
    # Создаем подключение к базе данных
    engine = create_engine(database_url)

    # Создаем таблицы на основе моделей, если их еще нет
    Base.metadata.create_all(engine)

    # Создаем сессию для взаимодействия с базой данных
    Session = sessionmaker(bind=engine)
    session = Session()

    return session

def get_user_by_id(session, user_id):
    return session.query(User).filter_by(user_id=user_id).first()

# Функция для создания нового пользователя
def create_user(session, user_id, user_name):
    new_user = User(user_id=user_id, user_name=user_name)
    session.add(new_user)
    session.commit()

def update_user_points(session, user, points):
    """
    Обновить количество очков пользователя.
    """
    user.scores += points
    session.commit()