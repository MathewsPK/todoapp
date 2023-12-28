from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from datetime import datetime
from .forms import todoforms

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')
        duetime = request.POST.get('duetime', '')
        obj = Todo(title=title, description=description, due_date=duetime)
        obj.save()
        return render(request, 'confirmation.html')
    tasks = Todo.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def tasks(request):
    tasks = Todo.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

def update_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id)

    if request.method == 'POST':
        form = todoforms(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = todoforms(instance=task)

    return render(request, 'update_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('tasks')

    return render(request, 'delete_task.html', {'task': task})
