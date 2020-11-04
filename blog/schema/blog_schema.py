import graphene
from graphene_django.types import DjangoObjectType
from blog.models import Blog as BlogModel

class Blog(DjangoObjectType):
    class Meta:
        model = BlogModel
