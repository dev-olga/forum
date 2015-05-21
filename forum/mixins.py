from django.views.generic import base
from django.views import generic
from django.http import JsonResponse

from forum import models


class CategoriesContextMixin(base.ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(CategoriesContextMixin, self).get_context_data(**kwargs)
        context['categories'] = models.Category.objects.all()
        return context


class AjaxFormMixin(generic.FormView):
    def form_valid(self, form):
        response = super(AjaxFormMixin, self).form_valid(form)
        if self.request.is_ajax():
            return JsonResponse({'response': '', 'is_valid': True, 'success_url': self.get_success_url()}, status=200)
        else:
            return response

    def form_invalid(self, form):
        response = super(AjaxFormMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse({'response': response.rendered_content, 'is_valid': False}, status=200)
        else:
            return response


class ModalDialogMixin(base.ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(ModalDialogMixin, self).get_context_data(**kwargs)
        context['show_buttons'] = not self.request.is_ajax()
        return context