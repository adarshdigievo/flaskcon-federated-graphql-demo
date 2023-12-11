import strawberry
from models import Session, Post
from .types import PostType, UserType


@strawberry.type
class Query:
    @strawberry.field
    def post(self, id: strawberry.ID) -> PostType:
        with Session() as session:
            post = session.query(Post).get(int(id))

        user = UserType(id=str(post.user))
        return PostType(id=post.id, title=post.title, content=post.content, user=user)

    @strawberry.field
    def posts(self) -> list[PostType]:
        with Session() as session:
            posts = session.query(Post).all()
        return [PostType(id=post.id, title=post.title, content=post.content, user=UserType(id=str(post.user))) for post
                in posts]
