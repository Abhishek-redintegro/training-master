import graphene
import blog.schema.schema as Blog

class Query(Blog.Query, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")



class Mutations(Blog.Mutations, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutations)