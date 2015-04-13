from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {'title': 'Forum'}
    return render(request, 'forum/index.html', context)


def subcategory(request):
    context = {'title': 'Forum'}
    return render(request, 'forum/subcategory.html', context)

def thread(request):
    context = {'title': 'Forum'}
    return render(request, 'forum/thread.html', context)




