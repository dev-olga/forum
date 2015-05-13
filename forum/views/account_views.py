from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.utils.functional import lazy
from django.utils.http import is_safe_url
from django.contrib import auth
from django.contrib.auth import logout
from django.shortcuts import redirect

from forum import forms
from forum.views.base_ajax_view import BaseAjaxView


class LoginView(BaseAjaxView):
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

            return super(LoginView, self).form_valid(form)


def logout_view(request, redirect_to=''):
    logout(request)
    if redirect_to:
        return redirect(redirect_to)
    return redirect(reverse('forum:index'))


class RegistrationView(BaseAjaxView):
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
