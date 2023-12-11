from models import Session, Post, engine, Base

Base.metadata.create_all(engine)

posts = [
    Post(title='First Post', content='Hello World!', user=1),
    Post(title='New Blog Post', content='This is the second post', user=2),
    Post(title='GraphQL and Flask', content='This is the third post', user=1),
]
with Session() as session:
    session.add_all(posts)
    session.commit()

session.close()
