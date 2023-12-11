import strawberry


@strawberry.type
class UserType:
    id: strawberry.ID
    name: str


@strawberry.type
class PostType:
    id: strawberry.ID
    title: str
    content: str

    @strawberry.field
    def summary(self) -> str:
        return f"{self.content[:10]}..." if len(self.content) > 10 else self.content

    @strawberry.field
    def created_by(self) -> UserType:
        print("Resolving created_by field")
        return UserType(id=1, name="John Doe")
