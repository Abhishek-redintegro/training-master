import graphene
from graphene_django.types import DjangoObjectType
from blog.models import Person as PersonModel


class Person(DjangoObjectType):
    class Meta:
        model = PersonModel


class CreatePerson(graphene.Mutation):
    class Arguments:
        u_name = graphene.String(required=True)
        u_desc = graphene.String(required=True)
        u_phone_no = graphene.String(required=True)
        u_email = graphene.String(required=True)
        u_password = graphene.String(required=True)

    person = graphene.Field(Person)

    def mutate(self, info, u_name, u_desc, u_phone_no, u_email, u_password):
        new_person = PersonModel(
            u_name=u_name,
            u_desc=u_desc,
            u_phone_no=u_phone_no,
            u_email=u_email,
            u_password=u_password
        )
        new_person.save()
        return CreatePerson(person=new_person)

class UpdatePerson(graphene.Mutation):
    class Arguments:
        u_email = graphene.String(required=True)
        id = graphene.Int()
    
    message = graphene.String()

    def mutate(self,info,u_email,id):
        old_person = PersonModel.objects.get(pk=id)
        old_email = old_person.u_email
        old_person.u_email = u_email
        old_person.save()
        return UpdatePerson(message=f'Old Email:{old_email} New Email:{u_email} For Id:{id}')


class DeletePerson(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    message = graphene.String()

    def mutate(self,info,id):
        old_person = PersonModel.objects.get(pk=id)
        old_person.delete()
        return DeletePerson(message=f'Deleted Data For Id:{id}')
# mutation{
#   createPerson(uDesc:"Regular", uEmail:"Abhisshek@gmail.com",uName:"Abhishek",
#     uPassword :"ABSA1212", uPhoneNo: "7218983902")
#   {
#     person{
#       id
#     }
#   }
# }