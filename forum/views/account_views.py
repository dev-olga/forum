from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.utils.functional import lazy
from django.utils.http import is_safe_url

from django.shortcuts import redirect
from django.views.generic import FormView
from django.template.loader import render_to_string
from django.http import JsonResponse

from forum import forms


class BaseAccountView(FormView):
    def form_valid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'response': '', 'is_valid': True}, status=200)
        else:
            return super(BaseAccountView, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.is_ajax():
            rendered = render_to_string(template_name=self.template_name,
                                        context=self.get_context_data(form=form),
                                        request=self.request)
            return JsonResponse({'response': rendered, 'is_valid': False}, status=200)
        else:
            return super(BaseAccountView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(BaseAccountView, self).get_context_data(**kwargs)
        context['show_buttons'] = not self.request.is_ajax()
        return context


class LoginView(BaseAccountView):
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

            login(self.request, form.get_user())

            return super(LoginView, self).form_valid(form)


def logout_view(request, redirect_to=''):
    logout(request)
    if redirect_to:
        return redirect(redirect_to)
    return redirect(reverse('forum:index'))


class RegistrationView(BaseAccountView):
    """
    New user registration view
    """

    template_name = 'forum/account/registration.html'
    success_url = lazy(reverse, str)('forum:index')
    form_class = forms.UserCreationForm

    def form_valid(self, form):
        # Ensure the user-originating redirection url is safe.
        if not is_safe_url(url=self.success_url, host=self.request.get_host()):
            return HttpResponseRedirect(self.request.path)

        # Save the new user first
        form.save()
        # Get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']

        # Authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)

        return super(RegistrationView, self).form_valid(form)
