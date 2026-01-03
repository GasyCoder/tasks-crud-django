from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task


def task_list(request: HttpRequest) -> HttpResponse:
    q = request.GET.get("q", "").strip()
    tasks = Task.objects.all()
    if q:
        tasks = tasks.filter(title__icontains=q)
    return render(request, "tasks/task_list.html", {"tasks": tasks, "q": q})


def task_detail(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=pk)
    return render(request, "tasks/task_detail.html", {"task": task})


def task_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("tasks:detail", pk=task.pk)
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form, "mode": "create"})


def task_update(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect("tasks:detail", pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/task_form.html", {"form": form, "mode": "update", "task": task})


def task_delete(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("tasks:list")
    return render(request, "tasks/task_confirm_delete.html", {"task": task})
