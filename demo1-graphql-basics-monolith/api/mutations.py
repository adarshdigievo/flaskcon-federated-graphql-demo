import strawberry

from api.types import PostType
from models import Session, Post


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_post(self, title: str, content: str) -> PostType:
        with Session() as session:
            post = Post(title=title, content=content)
            session.add(post)
            session.commit()
            session.refresh(post)

        return post
