from models import Session, User, engine, Base

Base.metadata.create_all(engine)
session = Session()

# Adding users
users = [
    User(username='Alice', email='alice@example.com'),
    User(username='Bob', email='bob@example.com'),
]

session.add_all(users)
session.commit()
session.close()
