from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from ..models import *


class SubCategory(View):
    template_name = 'forum/subcategory.html'

    def get(self, request):
        try:
            subcategory = SubCategory.object.get(id=1)
        except ObjectDoesNotExist:
            pass
        categories = Category.objects.all()
        return render(request, self.template_name, {'categories': categories, 'subcategory': subcategory})