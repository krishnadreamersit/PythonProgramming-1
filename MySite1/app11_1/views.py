from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User # System Defined
from django.contrib.auth import authenticate

def index(request):
# Getting All Users
    users = User.objects.all()
    print(users)
    # for user in users:
    #     print(user)
    # return HttpResponse("Success!")

# Creating a New User
    # username
    # password
    # email
    # first_name
    # last_name
    tmp_user = None
    tmp_user = User.objects.get(username='krishna')
    result = ""
    # if tmp_user==None:
    #     user1 = User.objects.create_user(username='krishna', password='krishna', email='krishna@gmail.com', first_name='Krishna', last_name = 'Aryal')
    #     user1.save()
    #     # print("New user save successfully")
    #     result = "New user save successfully"
    # else:
    #     # print("User already exist")
    #     result = "User already exist"
    # return HttpResponse(result)

    user2 = User.objects.create_user(username='user2', password='user2')
    user2.email='user2@gmail.com'
    user2.first_name='Kiran'
    user2.last_name='Thapa'
    user2.save()
    return HttpResponse("Success")

# Update Password
#     user3 = User.objects.get(username='krishna')
#     user3.set_password('Krishna')
#     user3.save()
    #user3.delete()


# Authenticate User
    user = authenticate(username='admin', password='admin')
    if user is not None:
       print("TRUE")
    else:
       print("FALSE")
    return HttpResponse("Hello from app11_1.")

    # Task
    # Create an application which used to manage users. USER-CRUD Application
        # List all users
        # Filter users
        # Create new user
        # Search user
        # Edit/Update user
        # Delete user
