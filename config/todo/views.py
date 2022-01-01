from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Todo

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello World</h>")


class TodoList(ListView):
    # models.pyで定義した「Todo」クラス→データベースにつながっている
    model = Todo
    context_object_name = "tasks"

class TodoDetail(DetailView):
    model = Todo
    context_object_name = "task"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'Todo Detail'
        context['message'] = '忘れずに完了させましょう'
        return context

class TodoCreate(CreateView):
    model = Todo
    # fieldeで入力する項目を設定する。今回は「title」「description」「deadline」の全てを入力したいため「__all__」で全選択している
    fields = "__all__"
    # タスクが作成できたらreverse_lazy()でlistという名前のページに遷移させる
    # listは「todo_list.html」のことみたいだ
    success_url = reverse_lazy("list")

class TodoUpdate(UpdateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("list")

class TodoDelete(DeleteView):
    model = Todo
    context_object_name = "task"
    success_url = reverse_lazy("list")