from django.urls import path
from .views import TodoList, TodoDetail, TodoCreate, TodoUpdate, TodoDelete, TodoListAfterCreate, TodoListAfterUpdate, TodoListAfterDelete

urlpatterns = [
    # ユーザーがトップページにアクセスしたらTodoListを表示する、という処理
    # ここで「list」と名付けているため「todo_list」というhtmlファイルが必要になる
    path("", TodoList.as_view(), name="list"),
    # タスクに応じてURLを変更するため、各タスクに割り振られているpk(=primary key)を指定する
    # detail/<int:pk>と設定することで各タスクごとに詳細ページを表示できる
    # ここで「detail」と名付けているため「todo_detail」というhtmlファイルが必要になる
    path("detail/<int:pk>", TodoDetail.as_view(), name="detail"),
    # 個別のタスクを選ぶ必要がないためcreate/にアクセスすればOKと設定する
    # nameはcreateだが、ユーザーに返すページはtodo_create.htmlではなく「todo_form.html」
    path("create/", TodoCreate.as_view(), name="create"),
    # タスクを編集するには個別タスクを選択する必要がある
    path("update/<int:pk>", TodoUpdate.as_view(), name="update"),
    # タスクを削除するには個別タスクを選択する必要がある
    # nameはdeleteだが、ユーザーに返すページはtodo_delete.htmlではなく「todo_confirm_delete.html」
    path("delete/<int:pk>", TodoDelete.as_view(), name="delete"),

    path("aftercreate/", TodoListAfterCreate.as_view(), name="aftercreate"),
    path("afterupdate/", TodoListAfterUpdate.as_view(), name="afterupdate"),
    path("afterdelete/", TodoListAfterDelete.as_view(), name="afterdelete"),

]