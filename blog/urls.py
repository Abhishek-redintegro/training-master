from django.urls import path
from . import views

urlpatterns = [
    # Blog Model
   
    path('', views.hello_world, name="hello_world"),
    path('allUsers', views.users_list, name="users_list"),#Hardcoded Data
    path('insUser', views.insert_user, name="insert_user"),#Return Same Hardcoded Data
    path('user/<int:id>', views.user_detail, name="user_detail"),#Return Same data wit inserted id
    path('blogs', views.blog_list, name="blog_list"),
    path('blog', views.insert_blog, name="insert_blog"),
    path('blog/<int:id>',views.update_blog, name="update_blog"),
    path('blog_delete/<int:id>', views.delete_blog, name="delete_blog"),
    # Person Model

    path('', views.hello_person, name="hello_person"),
    path('newPerson', views.insert_person, name="insert_person"),
    path('updatePerson/<int:id>',views.update_person, name="update_person"),
    path('deletePerson/<int:id>',views.delete_person, name="delete_person"),
    path('allPerson',views.person_list, name="person_list"),
    # path('person/<int:id>',views.person, name="person"),

]