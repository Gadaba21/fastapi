from dataclasses import dataclass

from repository import UserRepository
from schema import UserLoginSchema
from exception import UserNotFoundException, UserNotFoundPasswordException


@dataclass
class AuthService:
    user_repository: UserRepository

    def login(self, username: str, password: str) -> UserLoginSchema:
        user = self.user_repository.get_user_by_usetname(username)
        if not user:
            raise UserNotFoundException
        if user.password != password:
            raise UserNotFoundPasswordException
        return UserLoginSchema(user_id=user.id, access_token=user.access_token)
