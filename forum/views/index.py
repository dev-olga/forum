from django.shortcuts import render
from django.views.generic import View
from ..models import *


class Index(View):
    template_name = 'forum/index.html'

    def get(self, request):
        categories = Category.objects.all()
        subcategories = SubCategory.objects.all()
        return render(request, self.template_name, {'categories': categories, 'subcategories': subcategories})