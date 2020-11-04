import graphene
from graphene_django.types import DjangoObjectType
from blog.models import Person as PersonModel

class Person(DjangoObjectType):
    class Meta:
        model = PersonModel