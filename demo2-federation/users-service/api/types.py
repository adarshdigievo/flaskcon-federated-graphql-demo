import strawberry

from models import User, Session


@strawberry.federation.type(keys=["id"])
class UserType:
    id: strawberry.ID
    username: str
    email: str

    @classmethod
    def resolve_reference(cls, id: strawberry.ID):
        with Session() as session:
            user = session.query(User).get(int(id))
        return UserType(id=user.id, username=user.username, email=user.email)
