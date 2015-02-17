from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {'title': 'Forum'}
    return render(request, 'forum/index.html', context)


