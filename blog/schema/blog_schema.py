import graphene
from graphene_django.types import DjangoObjectType
from blog.models import Blog as BlogModel
from django.utils import timezone


class Blog(DjangoObjectType):
    class Meta:
        model = BlogModel


class CreateBlog(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        posted_by = graphene.String()

    blog = graphene.Field(Blog)

    def mutate(self, info, name, description, posted_by):
        new_blog = BlogModel(
            name=name,
            description=description,
            posted_by=posted_by,
            posted_on=timezone.now()
        )
        new_blog.save()
        return CreateBlog(blog=new_blog)


class UpdateBlog(graphene.Mutation):
    class Arguments:
        description = graphene.String(required=True)
        id = graphene.Int()

    message = graphene.String()

    def mutate(self, info, description, id):
        old_blog = BlogModel.objects.get(pk=id)
        old_desc = old_blog.description
        old_blog.description = description
        old_blog.save()
        return UpdateBlog(message=f'Old Description:{old_desc} New Description:{description} For Id:{id}')


class DeleteBlog(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    message = graphene.String()

    def mutate(self, info, id):
        old_blog = BlogModel.objects.get(pk=id)
        old_blog.delete()
        return DeleteBlog(message=f'Deleted Data For Id:{id}')