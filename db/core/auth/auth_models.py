from sqlalchemy import Column, Integer, String, ARRAY

from db.models import Base

class User(Base):
    __tablename__ = 'users'  # Имя таблицы в базе данных

    user_id = Column(Integer, primary_key=True, autoincrement=True)  # Уникальный идентификатор пользователя
    user_name = Column(String(255), nullable=True)  # Имя пользователя
    scores = Column(Integer, default=0)  # Очки пользователя, по умолчанию 0
    active_lessons = Column(ARRAY(Integer), nullable=True)  # Список активных уроков как массив чисел

    def __repr__(self):
        return f"<User(user_id={self.user_id}, user_name='{self.user_name}', scores={self.scores}, active_lessons={self.active_lessons})>"


