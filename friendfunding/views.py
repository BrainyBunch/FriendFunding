from django.shortcuts import render, redirect
from django.http import JsonResponse
from pyasn1_modules.rfc2459 import Time
from .models import User, Goal
from .forms import UserForm, GoalForm
from rest_framework import generics
import pyrebase 
import random
from django.contrib import auth

from .serializers import UserSerializer, GoalSerializer


# firebaseConfig = {    
#     "apiKey": "AIzaSyCd8K3DWSUID6pRZEP3n-cFwvnIBr6maz4",
#     "authDomain": "friendfunding-b16a2.firebaseapp.com",
#     "databaseURL": "https://friendfunding-b16a2-default-rtdb.firebaseio.com",
#     "projectId": "friendfunding-b16a2",
#     "storageBucket": "friendfunding-b16a2.appspot.com",
#     "messagingSenderId": "409268289779",
#     "appId": "1:409268289779:web:bf695d06dcb1dd16f17786",
#     "measurementId": "G-KFH3H81R3G"
#     }

# firebase = pyrebase.initialize_app(firebaseConfig)

# authe = firebase.auth()
# database = firebase.database()

# # ===================== Open the login 
# def login(request):
#     return render(request,"login.html")

# # ===================== opens to the home page if successful
# def postlogin(request):
#     email = request.POST.get("email")
#     password = request.POST.get("password")
#     try:
#         user =  authe.sign_in_with_email_and_password(email, password)
#     except: 
#         # alerts if they have the wrong password or user
#         message = "invalid credentials"
#         return render(request, 'login.html', {"messg":message})
#     #  printing only the token
#     print(user['idToken'])
#     #  creating a session for the user 
#     session_id = user['idToken']
#     request.session['uid']=str(session_id)
#     return render(request, 'welcome.html', {"e":email})

# # ===================== opens form for signing up
# def signUp(request):
#     return render(request,"signup.html")

# # ===================== opens to the home page if successful
# def postsignup(request):
#     name = request.POST.get("name")
#     email = request.POST.get("email")
#     password = request.POST.get("password")
#     confirm_password = request.POST.get("confirm_password")
#     print(password)
#     print(confirm_password)
#     if password == confirm_password:
#         user = authe.create_user_with_email_and_password(email, password)
#         uid = user['localId']
#         data = {"name": name, "status":"1"}
#         database.child("users").child(uid).child("details").set(data)

#         return render(request,'welcome2.html', {"e": email})
#     elif(password != confirm_password):
#         message = "Password was not entered correctly!"
#         return render(request, "signup.html", {"messg":message})
#     else: 
#         message = "Email has already been used! Please go to login"
#         return render(request, "login.html", {"message" :message})
    

# # ===================== creating the logout button
# def logout(request):
#     auth.logout(request)
#     return render(request, "login.html")

# def rando(request):
#     time = request.GET.get("z")
#     idtoken = request.session['uid']
#     a = authe.get_account_info(idtoken)
#     a = a['users']
#     a = a[0]
#     a = a['localId']

#     saved = []
#     number = random.randint(1,50)
#     saved.append(number)

#     saved_random = database.child('users').child(a).child('goal').child(time).child('saved').get().val()

#     print(number)
#     print(saved)
#     print(saved_random)
    
#     return render(request, "random.html", {"n":number})

# def create(request):
#     return render(request, "create.html")

# def postcreate(request):

# #  this is to get time it was added for the goals
#     import time 
#     from datetime import datetime, timezone
#     import pytz

# # getting the time zone from the timezone that i put 
#     tz = pytz.timezone('US/Pacific')
#     time_now = datetime.now(timezone.utc).astimezone(tz)
#     millis = int(time.mktime(time_now.timetuple()))
#     print("mili " + str(millis))

#     goal = request.POST.get('goal')
#     description = request.POST.get('description')
#     price = request.POST.get('price')
#     saved = request.POST.get('saved')

#     # getting the account info based on the id token
#     idtoken = request.session['uid']
#     a = authe.get_account_info(idtoken)
#     a = a['users']
#     a = a[0]
#     a = a['localId']
#     print("info " + str(a))

#     data = {
#         "goal": goal,
#         "description": description,
#         "price": price,
#         "saved": saved
#     }
        
#         # sending it to the database
#     database.child('users').child(a).child('goal').child(millis).set(data)

#     # getting the name of the user from the database and its children
#     name = database.child('users').child(a).child('details').child('name').get().val()
#     return render(request, 'welcome.html', {"e" : name})

# # =========== view for the goals
# def check(request):
#     import datetime

#     idtoken = request.session['uid']
#     a = authe.get_account_info(idtoken)
#     a = a['users'] 
#     a = a[0]
#     a = a['localId']

#     timestamps = database.child('users').child(a).child('goal').shallow().get().val()
#     #  SHALLOW IS USED TO GET A KEY
#     list_time = []
#     # iterating between all the goals in the users profile
#     for i in timestamps:
#         list_time.append(i)

#     list_time.sort(reverse=True)
#     print(list_time)
#     # iterating through the goals and getting the name of each goal
#     goals = []
#     for i in list_time: 
#         go = database.child('users').child(a).child('goal').child(i).child('goal').get().val()
#         goals.append(go)
#     print(goals)

#     # getting the saved amount 
#     saved = []
#     for i in list_time:
#         save = database.child('users').child('goal').child(i).child('saved').get().val()
#         saved.append(save)
#     print(saved)
# # gives the dates that the goal was made :) 
#     date = []
#     for i in list_time: 
#         i = float(i)
#         dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
#         date.append(dat)
#     print(date)

# #  combining all the lists
#     comb_list = zip(list_time, goals, saved, date)
#     name = database.child('users').child(a).child('details').child('name').get().val()
#     print(comb_list)
#     return render(request, "check.html", {'comb_list': comb_list, "e": name})

# def post_check(request):
#     import datetime
#     # getting the z from the check.html
#     time = request.GET.get("z")
#     idtoken = request.session['uid']
#     a = authe.get_account_info(idtoken)
#     a = a['users'] 
#     a = a[0]
#     a = a['localId']

#     goal = database.child('users').child(a).child('goal').child(time).child('goal').get().val()
#     description = database.child('users').child(a).child('goal').child(time).child('description').get().val()
#     price = database.child('users').child(a).child('goal').child(time).child('price').get().val()
#     saved = database.child('users').child(a).child('goal').child(time).child('saved').get().val()
#     i = float(time)
#     dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
#     name = database.child('users').child(a).child('details').child('name').get().val()

#     return render(request, "post_check.html", {'g': goal, "d": description, 'p': price, 's':saved, 'date': dat, "e":name})

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GoalList(generics.ListCreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class GoalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer








# -------------------------------------------
# LISTS
# def user_list(request):
#     user = User.objects.all()
#     user = user.order_by('name')
#     return render(
#         request, 
#         'friendfunding/user_list.html',
#         {'Users':user},
#         )

# def goal_list(request):
#     goal = Goal.objects.all()
#     return render(
#         request, 
#         'friendfunding/goal_list.html',
#         {'Goals':goal}
#         )
# # -------------------------------------------
# # Details
# def user_detail(request, pk):
#     try:
#         user = User.objects.get(id=pk)
#     except:
#         user= {
#             'name':"no User found",
#             'nationality':'with id{pk}'
#         }
#         print(f"artist with od={pk} didnt work")
#     return render(
#         request, 
#         'friendfunding/user_detail.html', 
#         {'user':user})
# def goal_detail(request, pk):
#     goal = Goal.objects.get(id=pk)
#     return render(request, 'friendfunding/goal_detail.html', {'goal': goal})
# # -------------------------------------------
# # CREATE
# def user_create(request):
#     if request.method == 'POST':
#         print(request.POST)
#         form = UserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect('user_detail', pk=user.pk)
#     else:
#         form = UserForm()
#     return render(request, 'friendfunding/user_form.html', {'form':form})
# def goal_create(request):
#     if request.method == 'POST':
#         print(request.POST)
#         form = GoalForm(request.POST)
#         if form.is_valid():
#             goal = form.save()
#             return redirect('goal_detail', pk=goal.pk)
#     else:
#         form = GoalForm()
#     return render(request, 'friendfunding/goal_form.html', {'form':form})
# # -------------------------------------------
# # DELETE
# def user_delete(request, pk):
#     User.objects.get(id=pk).delete()
#     return redirect('user_list')

# def goal_delete(request, pk):
#     Goal.objects.get(id=pk).delete()
#     return redirect('goal_list')
# # -------------------------------------------
# # EDIT
# def user_edit(request, pk):
#     user = User.objects.get(pk=pk)
#     if request.method == "POST":
#         form = UserForm(request.POST, instance=user)
#         if form.is_valid():
#             user = form.save()
#             return redirect('user_detail', pk=user.pk)
#     else:
#         form = UserForm(instance=user)
#     return render(request, 'friendfunding/user_form.html', {'form':form})


# def goal_edit(request, pk):
#     goal = Goal.objects.get(pk=pk)
#     if request.method == "POST":
#         form = GoalForm(request.POST, instance=goal)
#         if form.is_valid():
#             goal = form.save()
#             return redirect('goal_detail', pk=goal.pk)
#     else:
#         form = GoalForm(instance=goal)
#     return render(request, 'friendfunding/goal_form.html', {'form':form})

