from django.urls import path
from todolist.views import show_todolist
from todolist.views import create_task
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import delete_task
from todolist.views import toggle_status
from todolist.views import show_json
from todolist.views import add_task

app_name = "todolist"

urlpatterns = [
    path('', show_todolist, name = 'show_todolist'),
    path('create-task/', create_task, name = 'create_task'),
    path('register/', register, name = 'register'),
    path('login/', login_user, name = 'login_user'),
    path('logout/', logout_user, name = 'logout_user'),
    path('toggle-status/<int:id>', toggle_status, name = 'toggle_status'),
    path('delete-task/<int:id>/', delete_task, name = 'delete_task'),
    path('json/', show_json, name = 'show_json'),
    path('add/', add_task, name="add_task"),
]