"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('tasks/', tasks, name='tasks'),
    path('tasks_completed/', tasks_completed, name='tasks_completed'),
    path('logout/', signout, name='logout'),
    path('signin/', signin, name='signin'),
    path('tasks/create/', create_task, name='create_task'),
    path('tasks/detail/<int:task_id>/', task_detail, name='task_detail'),
    path('tasks/detail/<int:task_id>/complete', complete_task, name='complete_task'),
    path('tasks/detail/<int:task_id>/delete', delete_task, name='delete_task'),
]
