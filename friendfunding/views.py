from django.shortcuts import render

# Create your views here.
def user_create(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_detail', pk=user.pk)
        else:
            form = userForm()
    else:
        form = userForm()
    return render(request, 'tunr/user_form.html', {'form':form})

def user_edit(request, pk):
    user = user.objects.get(k=pk) #Todo.findById(matchXXX)
    if request.method == "POST":
        form = userForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = userForm(instance=user)
    return render(request, 'tunr/user_form.html', {'form': form})

def user_delete(request, pk):
    user.objects.get(id=pk).delete()
    return redirect('user_list')


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'tunr/song_list.html', {'songs': songs})

def song_detail(request, pk):
    song = Song.objects.get(id=pk)
    return render(request, 'tunr/song_detail.html', {'song': song})

def user_detail(request, pk):
    
    try:
        user = user.objects.get(id=pk)
    except:
        user = {
            'name': "No user found", 
            'nationality': f'with id {pk}'
            }
        print(f"user with id={pk} didn't work")
    
    return render(request, 'tunr/user_detail.html', {'user': user})