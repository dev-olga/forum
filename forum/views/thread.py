from django.shortcuts import render


def thread(request):
    context = {'title': 'Forum'}
    return render(request, 'forum/thread.html', context)




