import strawberry
from models import Session, User
from .types import UserType


@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: strawberry.ID) -> UserType:
        with Session() as session:
            user = session.query(User).get(int(id))
        return user

    @strawberry.field
    def users(self) -> list[UserType]:
        with Session() as session:
            users = session.query(User).all()
        return users
