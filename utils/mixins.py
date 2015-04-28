from django.http import JsonResponse
from django.views.generic import FormView


class AjaxResponseMixin(FormView):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxResponseMixin, self).form_invalid(form)
        if self. request. is_ajax():
            return JsonResponse(form. errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'response': 'ok'
            }
            return JsonResponse(data)
        else:
            return response