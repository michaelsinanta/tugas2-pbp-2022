from webbrowser import get
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.models import Task
from todolist.forms import TaskForm

# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)
    username = request.user
    context = {
        'list_todolist': data_todolist,
        'username': username,
    }
    return render(request, "todolist.html", context)

@login_required(login_url="/todolist/login/")
def create_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            listform = form.save(commit = False)
            listform.user = request.user
            listform.save()
            form.save()
            return redirect("todolist:show_todolist")
    context = {"forms": form,}
    return render(request, "create_task.html", context)

@login_required(login_url="/todolist/login/")
def delete_task(request, id):
    data_delete = Task.objects.get(pk = id)
    data_delete.delete()
    return redirect("todolist:show_todolist")

@login_required(login_url="/todolist/login/")
def toggle_status(request, id):
    data_toggle = Task.objects.get(pk = id)
    if data_toggle.is_finished :
        data_toggle.is_finished = False
    else :
        data_toggle.is_finished = True
    data_toggle.save()
    return redirect("todolist:show_todolist")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response