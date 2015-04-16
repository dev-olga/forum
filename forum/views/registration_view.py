from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
# from django.views.generic import View
# from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login
from django.utils.functional import lazy
from django.views.generic import FormView

from forum import forms

#
# class RegistrationView(View):
#     template_name = 'forum/register.html'
#
#     def get(self, request):
#         return render(request, self.template_name, {'form': forms.UserCreationForm()})
#
#     def post(self, request):
#         form = forms.UserCreationForm(request.POST)
#         if not form:
#             return redirect(reverse('forum:index'))
#
#         if form.is_valid():
#             user = form.save()
#             authenticate(username=user.username, password=user.password)
#             return redirect(reverse('forum:index'))
#
#         return render(request, self.template_name,{'form': form})


class RegistrationView(FormView):

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