from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User, Goal
from .forms import UserForm, GoalForm
from rest_framework import generics
from rest_framework import permissions
import random

randomFunc = random
# from .serializers import UserSerializer, GoalSerializer

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]



# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]


# class GoalList(generics.ListCreateAPIView):
#     queryset = Goal.objects.all()
#     serializer_class = GoalSerializer
#     permission_classes = [permissions.AllowAny]



# class GoalDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Goal.objects.all()
#     serializer_class = GoalSerializer
#     permission_classes = [permissions.AllowAny]


# -------------------------------------------
# LISTS
def user_list(request):
    user = User.objects.all()
    user = user.order_by('name')
    return render(
        request, 
        'friendfunding/user_list.html',
        {'Users':user},
        )

def goal_list(request):
    goal = Goal.objects.all()
    return render(
        request, 
        'friendfunding/goal_list.html',
        {'goal':goal}
        )
# # -------------------------------------------
# # Details
def user_detail(request, pk):
    try:
        user = User.objects.get(id=pk)
    except:
        user= {
            'name':"no User found",
            'nationality':'with id{pk}'
        }
        print(f"artist with od={pk} didnt work")
    return render(
        request, 
        'friendfunding/user_detail.html', 
        {'user':user})

#  ========== making a array global to pass saved amount 

goal_saved = []
new_saved = []

def goal_detail(request, pk):
    goal = Goal.objects.get(id=pk)
    goal_saved.append(goal.amountsaved)
    print('===========')
    print(goal_saved)
    return render(request, 'friendfunding/goal_detail.html', {'goal': goal})

# # ------------------------------------------

# # RANDOM BUTTON GENERATOR 
def random(request):
    randArray = []
    number = randomFunc.randint(1,50)
    randArray.append(number)
    saved = goal_saved

    third = sum(randArray + saved)
    new_saved.append(third)

    print('====random number===')
    print(randArray)
    print('====saved number===')
    print(saved)
    print('====total=====')
    print(new_saved)


    goal_saved.pop()
    # goal_saved.pop()
    # goal_saved.pop()
    new_saved.pop()
    # new_saved.pop()
    # new_saved.pop()

    # output = number + saved
    # new_saved.append(output)
    
    # print(output)
    return render(request, "friendfunding/random.html", {'random':randArray, 'total': third})
# # -------------------------------------------
# # CREATE
def user_create(request):
    if request.method == 'POST':
        print('================')
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            print('==========')
            print(user)
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm()
    return render(request, 'friendfunding/user_form.html', {'form':form})
    
def goal_create(request):
    if request.method == 'POST':
        print(request.POST)
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save()
            # seeing if the goal information prints 
            print(goal)
            return redirect('goal_detail', pk=goal.pk)
    else:
        form = GoalForm()
    return render(request, 'friendfunding/goal_form.html', {'form':form})

# # -------------------------------------------
# # DELETE
def user_delete(request, pk):
    User.objects.get(id=pk).delete()
    return redirect('user_list')

def goal_delete(request, pk):
    Goal.objects.get(id=pk).delete()
    return redirect('goal_list')
# # -------------------------------------------
# # EDIT
def user_edit(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'friendfunding/user_form.html', {'form':form})


def goal_edit(request, pk):
    goal = Goal.objects.get(pk=pk)
    if request.method == "POST":
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            goal = form.save()
            return redirect('goal_detail', pk=goal.pk)
    else:
        form = GoalForm(instance=goal)
    return render(request, 'friendfunding/goal_form.html', {'form':form})

