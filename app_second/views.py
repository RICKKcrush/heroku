from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from . import models


# тут только "логика" - функции для обработки и возврат данных


def index(request):
    # return HttpResponse("Это чистая индекс страница")
    context = {

    }
    return render(request, 'app_second/pages/index.html', context)


def func(description, name="Apple"):
    pass


def home(request):
    context = {

    }
    return render(request, 'app_second/pages/home.html', context)


def login(request):
    context = {

    }
    return render(request, 'app_second/pages/login.html', context)


def about(request):
    context = {

    }
    return render(request, 'app_second/pages/about.html', context)


def origin_home(request):
    context = {

    }
    return render(request, 'app_second/pages/origin_home.html', context)


def todo_detail(request, todo_id):
    print(request)
    if request.method == "GET":
        print("это GET запрос")
    if request.method == "POST":
        print("это POST запрос")
    if request.method == "PUT":
        print("это PUT запрос")
    if request.method == "DELETE":
        print("это DELETE запрос")

    # print("request.method: ", request.method)
    # print("request.path: ", request.path)
    # print("request.headers: ", request.headers)
    # print("request.META: ", )

    # пробегаемся по ключам словаря
    # for key, value in request.META.keys():

    # пробегаемся по значениям словаря
    # for key, value in request.META.values():

    # пробегаемся по парам: ключ-значение
    # for key, value in request.META.items():
    #     print(f"{key}: {value}")
    # print("request.data: ", request.data)
    # print("request.GET: ", request.GET)

    is_completed = False
    if is_completed:
        pass
    else:
        pass

    list = [1, 2, 3]
    for i in list:
        index = list.index(i)
        # print(i)
        pass

    obj = models.Task.objects.get(id=todo_id)

    context = {
        "todo": obj
    }

    return render(request, 'app_second/pages/DetailTodo.html', context)


def todo_list(request):
    print(request)
    if request.method == "GET":
        print("это GET запрос")
    if request.method == "POST":
        print("это POST запрос")
    if request.method == "PUT":
        print("это PUT запрос")
    if request.method == "DELETE":
        print("это DELETE запрос")

    # print("request.method: ", request.method)
    # print("request.path: ", request.path)
    # print("request.headers: ", request.headers)
    # print("request.META: ", )

    # пробегаемся по ключам словаря
    # for key, value in request.META.keys():

    # пробегаемся по значениям словаря
    # for key, value in request.META.values():

    # пробегаемся по парам: ключ-значение
    # for key, value in request.META.items():
    #     print(f"{key}: {value}")
    # print("request.data: ", request.data)
    # print("request.GET: ", request.GET)

    is_completed = False
    if is_completed:
        pass
    else:
        pass

    list = [1, 2, 3]
    for i in list:
        index = list.index(i)
        # print(i)
        pass

    obj = models.Task.objects.all()

    print(f"obj: {obj}")
    print(f"obj count: {obj.count()}")

    context = {"list": obj}

    return render(request, 'app_second/pages/todo_list.html', context)


def todo_create(request):
    print("todo_create")
    if request.method == "POST":
        print("это POST запрос")

        # вызывается Exception (исключение)
        # title = request.POST["title"]
        title1 = request.POST.get("title", "заголовок по умолчанию")
        description1 = request.POST.get("description", "описание по умолчанию")

        obj = models.Task.objects.create(
            title=title1,
            description=description1
        )
        obj.save()


        # приём и обработка данных
    context = {}
    return render(request, 'app_second/pages/CreateTodo.html', context)

def todo_delete(request, todo_id):
    obj = models.Task.objects.get(id=todo_id)
    obj.delete()
    return redirect(reverse('todo_list', args=()))

def todo_update_status(request, todo_id):
    obj = models.Task.objects.get(id=todo_id)
    # obj.is_completed = not obj.is_completed
    if obj.is_completed:
        obj.is_completed = False
    else:
        obj.is_completed = True
    obj.save()
    return redirect(reverse('todo_list', args=()))