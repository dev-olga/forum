from django.views.generic import View, FormView
from django.views.generic import FormView
from django.template.loader import render_to_string
from django.http import JsonResponse

from forum import models
from forum import mixins


class BaseForumView(View):

    def _get_context(self):
        return {'categories': models.Category.objects.all()}


class BaseAjaxFormView(FormView):
    def form_valid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'response': '', 'is_valid': True}, status=200)
        else:
            return super(BaseAjaxFormView, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.is_ajax():
            rendered = render_to_string(template_name=self.template_name,
                                        context=self.get_context_data(form=form),
                                        request=self.request)
            return JsonResponse({'response': rendered, 'is_valid': False}, status=200)
        else:
            return super(BaseAjaxFormView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(BaseAjaxFormView, self).get_context_data(**kwargs)
        context['show_buttons'] = not self.request.is_ajax()
        return context