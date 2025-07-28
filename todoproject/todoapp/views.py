from datetime import date
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Task
from .forms import TaskForm


@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user).order_by('date')  # 👈 Only show user's tasks
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # 👈 Assign current user
            task.save()
        return redirect('/')

    today = date.today()
    return render(request, 'todoapp/index.html', {
        'tasks': tasks,
        'form': form,
        'today': today,
    })

from django.shortcuts import get_object_or_404

@login_required
def toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('/')
@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.user == request.user:
        task.delete()
    return redirect('/')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'todoapp/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'todoapp/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')