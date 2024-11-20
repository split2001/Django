from django.shortcuts import render
from django.http import HttpResponse  # для возврата http ответа пользователю
from .forms import UserRegister

# Create your views here.


def sign_up_by_django(request):
    users = ['teammate', 'pilot', 'fruit', 'spb1812']
    info = {}
    if request.method == 'POST':  # проверка запроса на GET или POST
        form = UserRegister(request.POST)  # создаем форму с данными
        if form.is_valid():
            username = form.cleaned_data['username']  # form.cleaned_data словарь, содержащий очищенные данные,
            # через который можно получить данные из формы
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if repeat_password != password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                return HttpResponse(f'Приветствуем тебя,{username}!')
    else:
        form = UserRegister()  # если метод запроса не 'POST', то создаем пустую форму

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', context=info)


def sign_up_by_html(request):
    users = ['teammate', 'pilot', 'fruit', 'spb1812']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if repeat_password != password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            return HttpResponse(f'Приветствуем тебя,{username}!')
    return render(request, 'fifth_task/registration_page.html', context=info)
