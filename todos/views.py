

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from .models import Todo
from django.urls import reverse_lazy
from datetime import date
from django.shortcuts import get_object_or_404, redirect



def home(request):
    return render(request, "home.html")


class TodoListView(ListView):
    model=Todo


class TodoCreateView(CreateView):
    model=Todo
    fields=["title","deadline"]
    success_url=reverse_lazy("todo_list")



class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'deadline']
    success_url = reverse_lazy('todo_list')