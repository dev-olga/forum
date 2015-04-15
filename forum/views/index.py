from django.shortcuts import render
from django.views.generic import View
from forum import models


class Index(View):
    template_name = 'forum/index.html'

    def get(self, request):
        categories = models.Category.objects.all()
        latest_post = models.Post.objects.order_by('date').reverse().all()[0:3]
        return render(request, self.template_name, {'categories': categories, 'latest_post': latest_post})