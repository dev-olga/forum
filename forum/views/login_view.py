from django.core.urlresolvers import reverse
from django.contrib import auth
from django.http import HttpResponseRedirect, JsonResponse
from django.utils.functional import lazy
from django.utils.http import is_safe_url
from django.views.generic import FormView
from forum import forms


class LoginView(FormView):
    """
    Login view
    """

    template_name = 'forum/account/login.html'
    success_url = lazy(reverse, str)('forum:index')
    form_class = forms.AuthenticationForm

    def form_valid(self, form, **kwargs):
        if form.is_valid():
            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=self.success_url, host=self.request.get_host()):
                return HttpResponseRedirect(self.request.path)

            auth.login(self.request, form.get_user())
            if self.request.is_ajax():
                JsonResponse({'errors': '', 'redirect_to': self.success_url}, status=200)
            else:
                return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'errors': 'Your username and password didn\'t match. Please try again.'}, status=200)
        else:
            return super(LoginView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['show_button'] = not self.request.is_ajax()
        return context

