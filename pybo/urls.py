"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views FV
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views CV
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from  django.contrib import  admin
from  django.urls import  path, include
from  pybo import  views

#url 네임스페이스 지정
app_name='pybo'

urlpatterns = [
    path('', views.index, name='home'), #http://127.0.0.1:8000/pybo/' + ''=>http
    path('greet/', views.greet, name='greet'),
    path('<int:question_id>/', views.detail, name='details'),
    path('answer/create/<int:question_id>/', views.answer_create, name="answer_create"),
    path('question/create/', views.question_create, name="question_create")
]
