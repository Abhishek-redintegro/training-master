import graphene
import blog.schema.schema as Blog

class Query(Blog.Query, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

schema = graphene.Schema(query=Query)