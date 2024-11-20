"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from task2.views import text2, Text1
from django.views.generic import TemplateView
from task4.views import menu, game, cart, platform
from task5.views import sign_up_by_html, sign_up_by_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('function/', text2),
    path('class/', Text1.as_view()),  # метод .as_view для запуска класса как функции
    path('ttt', platform),
    path('games/', game),
    path('cart/', cart),
    path('platform/', platform),
    path('', sign_up_by_html),
    path('django_sign_up/', sign_up_by_django)
]
#  path('class/', TemplateView.as_view(template_name = 'second_task/text1.html'))
