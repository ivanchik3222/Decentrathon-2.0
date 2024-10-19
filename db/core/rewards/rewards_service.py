
from db.db_session import get_user_by_id, update_user_points

def add_points_to_user(session, user_id, points):
    """
    Начисляет очки пользователю.
    :param user_id: ID пользователя в Telegram.
    :param points: Количество очков, которое нужно начислить.
    """
    user = get_user_by_id(session, user_id)
    if user:
        update_user_points(session, user, points)
