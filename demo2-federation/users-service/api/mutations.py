import strawberry
from models import Session, User
from .types import UserType


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, username: str, email: str) -> UserType:
        user = User(username=username, email=email)
        with Session() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
        return UserType(id=user.id, username=user.username, email=user.email)
