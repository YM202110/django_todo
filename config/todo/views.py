from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, FormView
from .models import Todo
from .forms import TodoForm, AnalysisPeriodForm

from django.urls import reverse_lazy, reverse
from numpy import character

from . import graph
import datetime
from datetime import timedelta
import pandas as pd
from django.utils.timezone import localtime

from django.shortcuts import render

"""
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
"""


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
    # template_name = 'todo/todo_form.html'
    model = Todo
    # form経由でmodelを編集するため、どのformと紐づけるか定義
    form_class = TodoForm
    # fieldで入力する項目を設定する。今回は「title」「description」「deadline」の全てを入力したいため「__all__」で全選択している
    # 1つずつ選択する場合の書き方は「fields = ['title', 'description', 'deadline']」。models.pyの定義通り。
#    fields = "__all__"
    # タスクが作成できたらreverse_lazy()でlistという名前のページに遷移させる
    # listは「todo_list.html」のことみたいだ
    success_url = reverse_lazy("aftercreate")

    # detailに遷移させる場合は、個別ページのurlが必要だから以下のようにする
    # def get_success_url(self):
    #     return reverse_lazy("detail", kwargs={'pk':self.object.pk})
    
    # csrf_tokenを無効化したいときは以下のコードを記載する
    # @method_decorator(csrf_exempt)
    # def dispatch(self, *args, **kwargs):
    #     return super(TodoCreate, self).dispatch(*args, **kwargs)

class TodoUpdate(UpdateView):
    model = Todo
    form_class = TodoForm
#    fields = "__all__"
    success_url = reverse_lazy("afterupdate")

class TodoDelete(DeleteView):
    model = Todo
    context_object_name = "task"
    success_url = reverse_lazy("afterdelete")



class TodoListAfterCreate(ListView):
    template_name = "todo/after_create.html"
    model = Todo
    context_object_name = "tasks"

class TodoListAfterUpdate(ListView):
    template_name = "todo/after_update.html"
    model = Todo
    context_object_name = "tasks"

class TodoListAfterDelete(ListView):
    template_name = "todo/after_delete.html"
    model = Todo
    context_object_name = "tasks"


class TodoAnalysis(FormView):
    form_class = AnalysisPeriodForm
    template_name = "todo/todo_analysis.html"
    
    def form_valid(self, form):
        # formのclean関数を経てから日付を受取る
        period = form.cleaned_data
        start_day = period["start_day"]
        end_day   = period["end_day"]
        # グラフに表示する日数を指定する=for文で何回ループ処理するか
        N = (end_day - start_day).days + 1
        # 指定期間の辞書を作る
        tasks = {}
        for i in range(N):
            date = start_day + timedelta(i)
            tasks[date] = 0
        # Todoモデルのクエリセットからupdated_at(=最終更新日)を取得してdate型にする
        qs = Todo.objects.all()
        update_list = [localtime(ele.updated_at) for ele in qs if str(ele.status) == "完了済"]
        dataf = pd.DataFrame({'time': update_list})
        dataf['time'] = pd.to_datetime(dataf['time']).dt.date

        for ele in dataf['time']:
            if ele in tasks:
                tasks[ele] += 1

        # グラフのx軸とy軸用のデータを格納する
        x = [x for x in tasks.keys()]
        y = [y for y in tasks.values()]
        chart = graph.Plot_Graph(x, y)

        # ここで引数に渡せば、上記のどの変数もテンプレートに渡せる（以下ではchartをchart(オレンジ)の名前で渡しているし、formもformで送ってる）
        ctxt = self.get_context_data(chart=chart, form=form, y=y)

        return self.render_to_response(ctxt)

