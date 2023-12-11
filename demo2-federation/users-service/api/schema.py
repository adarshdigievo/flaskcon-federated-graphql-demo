import strawberry

from api.mutations import Mutation
from api.queries import Query
from api.types import UserType

schema = strawberry.federation.Schema(query=Query, mutation=Mutation, types=[UserType])
