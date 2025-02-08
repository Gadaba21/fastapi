from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db_session
from cache import get_redis_connection
from repository import UserRepository, BookRepository, BookCache
from service import UserService, AuthService



def get_books_repository(db_session: Session = Depends(
        get_db_session)) -> BookRepository:
    return BookRepository(db_session=db_session)


def get_books_cache_repository() -> BookCache:
    redis_connection = get_redis_connection()
    return BookCache(redis_connection)


def get_user_repository(db_session: Session = Depends(
        get_db_session)) -> UserRepository:
    return UserRepository(db_session=db_session)


def get_user_service(user_repository: UserRepository = Depends(
        get_user_repository)) -> UserService:
    return UserService(user_repository=user_repository)


def get_auth_service(user_repository: UserRepository = Depends(
        get_user_repository)) -> AuthService:
    return AuthService(user_repository=user_repository)
