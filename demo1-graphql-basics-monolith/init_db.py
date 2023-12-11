from models import Session, Post


def init_db():
    session = Session()
    # Sample data
    posts = [
        Post(title="Hello World", content="This is my first post!"),
        Post(title="GraphQL", content="Exploring GraphQL with Strawberry & Flask")
    ]
    session.add_all(posts)
    session.commit()


if __name__ == "__main__":
    init_db()
