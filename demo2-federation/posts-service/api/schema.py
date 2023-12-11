import strawberry

from api.queries import Query

schema = strawberry.federation.Schema(query=Query)
