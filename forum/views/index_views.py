from django.shortcuts import render
from django.views.generic import View
from forum import models
from django.db.models import Max


class IndexView(View):
    template_name = 'forum/index.html'

    def get(self, request):
        categories = models.Category.objects.all()
        latest_threads = models.Thread.objects.annotate(latest_post=Max('post__date'))\
            .order_by(max('latest_post', 'date')).reverse()[0:3]
        return render(request, self.template_name, {'categories': categories, 'latest_threads': latest_threads})