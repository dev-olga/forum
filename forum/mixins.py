from django.views.generic import base
from django.template.loader import render_to_string
from django.http import JsonResponse

from forum import models


class CategoriesContextMixin(base.ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(CategoriesContextMixin, self).get_context_data(**kwargs)
        context['categories'] = models.Category.objects.all()
        return context


class AjaxResponseMixin(object):
    def form_valid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'response': '', 'is_valid': True, 'success_url': self.get_success_url()}, status=200)
        else:
            return super(AjaxResponseMixin, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.is_ajax():
            rendered = render_to_string(template_name=self.template_name,
                                        context=self.get_context_data(form=form),
                                        request=self.request)
            return JsonResponse({'response': rendered, 'is_valid': False}, status=200)
        else:
            return super(AjaxResponseMixin, self).form_invalid(form)


class ModalDialogMixin(base.ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(ModalDialogMixin, self).get_context_data(**kwargs)
        context['show_buttons'] = not self.request.is_ajax()
        return context