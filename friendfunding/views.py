from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User, Goal
from .forms import UserForm, GoalForm
# -------------------------------------------
# LISTS
def user_list(request):
    user = User.objects.all()
    user = user.order_by('name')
    print(user)
    return render(
        request, 
        'friendfunding/user_list.html',
        {'user':user},
        )
def goal_list(request):
    goal = Goal.objects.all()
    return render(
        request, 
        'friendfunding/goal_list.html',
        {'goal':goal}
        )
# -------------------------------------------
# Details
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
def goal_detail(request, pk):
    goal = Goal.objects.get(id=pk)
    return render(request, 'friendfunding/goal_detail.html', {'goal': goal})
# -------------------------------------------
# CREATE
def user_create(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm()
    return render(request, 'friendfunding/user_form.html', {'form':form})
def goal_create(request):
    if request.method == 'POST':
        print(request.POST)
        form = GoalForm(request.POST)
        print(form)
        if form.is_valid():
            goal = form.save()
            return redirect('goal_detail', pk=goal.pk)
    else:
        form = GoalForm()
    return render(request, 'friendfunding/goal_form.html', {'form':form})
# -------------------------------------------
# DELETE
def user_delete(request, pk):
    User.objects.get(id=pk).delete()
    return redirect('user_list')
# -------------------------------------------
# EDIT
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
