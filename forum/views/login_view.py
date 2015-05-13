# from django.core.urlresolvers import reverse
# from django.contrib import auth
# from django.http import HttpResponseRedirect
# from django.utils.functional import lazy
# from django.utils.http import is_safe_url
# from forum import forms
# from forum.views.base_ajax_view import BaseAjaxView
#
#
# class LoginView(BaseAjaxView):
#     """
#     Login view
#     """
#
#     template_name = 'forum/account/login.html'
#     success_url = lazy(reverse, str)('forum:index')
#     form_class = forms.AuthenticationForm
#
#     def form_valid(self, form, **kwargs):
#         if form.is_valid():
#             # Ensure the user-originating redirection url is safe.
#             if not is_safe_url(url=self.success_url, host=self.request.get_host()):
#                 return HttpResponseRedirect(self.request.path)
#
#             auth.login(self.request, form.get_user())
#
#             return super(LoginView, self).form_valid(form)
#
