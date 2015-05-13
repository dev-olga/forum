from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import FormView
from django.template.loader import render_to_string


class BaseAjaxView(FormView):
    def form_valid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'invalid': '', 'redirect_to': str(self.success_url)}, status=200)
        else:
            return super(BaseAjaxView, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.is_ajax():
            rendered = render_to_string(template_name=self.template_name,
                                        context=self.get_context_data(form=form),
                                        request=self.request)
            return JsonResponse({'invalid': rendered}, status=200)
        else:
            return super(BaseAjaxView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(BaseAjaxView, self).get_context_data(**kwargs)
        context['show_button'] = not self.request.is_ajax()
        return context