from django.shortcuts import render


def subcategory(request):
    context = {'title': 'Forum'}
    return render(request, 'forum/subcategory.html', context)