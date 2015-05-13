from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, JsonResponse
from django.utils.functional import lazy
from django.utils.http import is_safe_url
from django.views.generic import FormView
from django.template.loader import render_to_string
from forum import forms


class RegistrationView(FormView):
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

        if self.request.is_ajax():
            return JsonResponse({'invalid': ''}, status=200)
        else:
            return super(RegistrationView, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.is_ajax():
            rendered = render_to_string(template_name=self.template_name,
                                        context=self.get_context_data(form=form),
                                        request=self.request)
            return JsonResponse({'invalid': rendered}, status=200)
        else:
            return super(RegistrationView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(RegistrationView, self).get_context_data(**kwargs)
        context['show_button'] = not self.request.is_ajax()
        return context