import graphene

import sources.schema

class Query(
    sources.schema.Query,
    graphene.ObjectType):
    # This class will inherit from multiple Queries
    pass

schema = graphene.Schema(query=Query)
# print(str(schema))