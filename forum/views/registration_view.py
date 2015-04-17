from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.utils.functional import lazy
from django.views.generic import FormView
from forum import forms


class RegistrationView(FormView):
    """
    New user registration form
    """

    template_name = 'forum/account/registration.html'
    success_url = lazy(reverse, str)('forum:index')
    form_class = forms.UserCreationForm

    def form_valid(self, form):
        #save the new user first
        form.save()
        #get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        #authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(RegistrationView, self).form_valid(form)