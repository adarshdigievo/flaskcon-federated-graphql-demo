import strawberry

from api.types import PostType
from models import Session, Post


@strawberry.type
class Query:
    @strawberry.field
    def get_posts(self) -> list[PostType]:
        with Session() as session:
            return session.query(Post).all()

    @strawberry.field
    def get_post_by_id(self, id: strawberry.ID) -> PostType:
        with Session() as session:
            return session.get(Post, id)
