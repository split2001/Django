from django.shortcuts import render
from django.views.generic import TemplateView  # базовый шаблон для наследования классов
# Create your views here.


def text2(request):
    return render(request, 'second_task/text2.html')


class Text1(TemplateView):
    template_name = 'second_task/text1.html'






