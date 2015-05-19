from forum import models
from django.views.generic import base


class CategoriesContextMixin(base.ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(CategoriesContextMixin, self).get_context_data(**kwargs)
        context['categories'] = models.Category.objects.all()
        return context