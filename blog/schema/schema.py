import graphene
from blog.schema.blog_schema import Blog, BlogModel
from blog.schema.person_schema import Person, PersonModel
from blog.schema.blog_schema import Blog, BlogModel, CreateBlog, UpdateBlog, DeleteBlog
from blog.schema.person_schema import Person, PersonModel, CreatePerson, UpdatePerson, DeletePerson


class Query(graphene.ObjectType):
    # Blog Models Start----------------
    allBlogs = graphene.List(Blog)
    blog = graphene.Field(Blog, id=graphene.Int(required=True))
    # Blog Models End----------------

    # Person Model Start------------------
    allPerson = graphene.List(Person)
    person = graphene.Field(Person, id=graphene.Int(required=True))
    # Person Model End-----------------

    # Blog
    def resolve_allBlogs(self, info):
        return BlogModel.objects.all()

    def resolve_blog(self, info, id):
        return BlogModel.objects.get(pk=id)

    # Person
    def resolve_allPerson(self, info):
        return PersonModel.objects.all()

    def resolve_person(self, info, id):
        return PersonModel.objects.get(pk=id)


class Mutations(graphene.ObjectType):
    create_blog = CreateBlog.Field()
    create_person = CreatePerson.Field()
    update_blog = UpdateBlog.Field()
    update_person = UpdatePerson.Field()
    delete_blog = DeleteBlog.Field()
    delete_person = DeletePerson.Field()