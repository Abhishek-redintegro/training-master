from django.http import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Blog, Person
from django.core import serializers
from django.utils import timezone


# Create your views here.

# Views For BLog /......
def hello_world(request):
    return HttpResponse("Hello World")


def users_list(request):  # Get -raw -jSON
    data = [
        {'name': "Sehal", 'email': 'seinsehal@gmail.com'},
        {'name': "Sein", 'email': 'sehal@redintegro.com'}
    ]
    # output[{"name": "Sehal", "email": "seinsehal@gmail.com"}, {"name": "Sein", "email": "sehal@redintegro.com"}]
    return JsonResponse(data, safe=False)


@csrf_exempt  # Post -raw -jSON data insert
@require_http_methods(['POST'])
def insert_user(request):
    data = json.loads(request.body.decode('utf-8'))
    return JsonResponse(data, safe=False)  # Same Inserted jSON Return


def user_detail(request, id):  # Hardcoded Data Return(Accept id As Param)
    data = {'name': "Sehal", 'email': 'seinsehal@gmail.com', 'id': id}
    return JsonResponse(data)  # Return Same data wit inserted id


def blog_list(request):  # Get -none(no data passed)
    data = Blog.objects.all()
    response = serializers.serialize("json", data)
    # all data from database
    return HttpResponse(response, content_type="application/json")


@csrf_exempt  # Take json as input/ Post -raw -jSON
@require_http_methods(['POST'])
def insert_blog(request):
    data = json.loads(request.body.decode('utf-8'))

    # if data['name'] == None:
    #     print("Error")

    new_blog = Blog(
        name=data['name'],
        description=data['description'],
        posted_by=data['postedBy'],
        posted_on=timezone.now()
    )

    new_blog.save()

    # return same jSON data and add that data in database
    return JsonResponse(data)


@csrf_exempt  # Update Discription
# Post -raw -jSON {"desciption":"Data/NewValue"}
@require_http_methods(['POST'])
def update_blog(request, id):
    data = json.loads(request.body.decode('utf-8'))
    old_blog = Blog.objects.get(pk=id)
    old_blog.description = data['description']
    old_blog.save()
    return JsonResponse(data)  # Output {"description": "Blog 1"}

@csrf_exempt
@require_http_methods(['POST'])
def delete_blog(request,id):
    old_blog = Blog.objects.get(pk=id)
    old_blog.delete()
    return HttpResponse("Record deleted")

# Views for Person/........


def hello_person(request):  # Empty Page - Hello World Message
    return HttpResponse("Hello World")

# Insert Data In Database


@csrf_exempt  # Take json as input/ Post -raw -jSON
@require_http_methods(['POST'])
def insert_person(request):
    data = json.loads(request.body.decode('utf-8'))

    new_person = Person(
        u_name=data['u_name'],
        u_desc=data['u_desc'],
        u_phone_no=data['u_phone_no'],
        u_email=data['u_email'],
        u_password=data['u_password']
    )
    new_person.save()
    # return same jSON data and add that data in database
    return JsonResponse(data)
# Update Data from Database(All Feilds)


@csrf_exempt  # Update Post -raw -jSON (updating feilds)
@require_http_methods(['POST'])
def update_person(request, id):
    data = json.loads(request.body.decode('utf-8'))
    old_person = Person.objects.get(pk=id)

    old_person.u_name = data['u_name']
    old_person.u_desc = data['u_desc']
    old_person.u_phone_no = data['u_phone_no']
    old_person.u_email=data['u_email']
    old_person.u_password=data['u_password']
    old_person.save()
    return JsonResponse(data)  # Output All passed data

@csrf_exempt #Post -none 
@require_http_methods(['POST'])
def delete_person(request,id):
    print(id)
    old_person = Person.objects.get(pk=id)
    old_person.delete()
    return HttpResponse(f'Record Deleted For id {id}')

def person_list(request):  # Get -none(no data passed)
    data = Person.objects.all()
    response = serializers.serialize("json", data)
    # all data from database
    return HttpResponse(response, content_type="application/json")

# def person(request,id):
#     data = Person.objects.get(pk=id)
#     response = serializers.serialize("json",data)
#     return HttpResponse(response, content_type="application/json")
    
# CRUD
# Create new model
# Fetch list of data
# Insert Data to DB
# Updated Data; model.save()
# Deleting Data; model.delete()

# Data To Add 
# {
#     "u_name" : "Neha",
#     "u_desc" : "Reguler",
#     "u_phone_no" : "9325485753",
#     "u_email" : "Neha07@gmail.com",
#     "u_password" : "Pa55w0rd@"
# }