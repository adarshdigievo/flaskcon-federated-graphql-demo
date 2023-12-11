import strawberry

from models import Session, Post


def resolve_user_post_count(root: 'UserType') -> int:
    post_count = 0
    with Session() as session:
        post_count = session.query(Post).filter(Post.user == root.id).count()
    return post_count


@strawberry.federation.type(keys=["id"])
class UserType:
    id: strawberry.ID
    posts_count: int = strawberry.field(resolver=resolve_user_post_count)
    

# The resolve reference function here can be ommitted since we wrote custom resolver for the 'posts_count' field,
# which is the only extra field other than the key field 'id'.

    # posts_count: int
    
    # @classmethod
    # def resolve_reference(cls, id: strawberry.ID):
    #     post_count = 0

    #     with Session() as session:
    #         post_count = session.query(Post).filter(Post.user == id).count()
    #     return UserType(id=id, posts_count=post_count)


@strawberry.type
class PostType:
    id: strawberry.ID
    title: str
    content: str
    user: UserType
