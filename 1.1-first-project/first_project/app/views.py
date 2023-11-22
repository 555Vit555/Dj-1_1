import os
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    # Получаем текущую рабочую директорию
    # current_dir = os.getcwd()
    #
    # # Получаем список файлов в текущей директории
    # file_list = " ".join(os.listdir(current_dir))
    #
    # # Возвращаем список файлов в качестве ответа
    list = os.listdir(path='.')
    file_list = '  '.join(list)

    return HttpResponse(file_list)
    #raise NotImplemented
