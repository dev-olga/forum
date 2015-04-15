from django.shortcuts import render
from django.views.generic import View
from forum import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class Thread(View):

    def get(self, request, id):
        return render(request, 'forum/thread.html')

    # #TODO login check
    # def post(self, request):
    #     form = forms.ThreadForm(request.POST)
    #     if not form:
    #         return HttpResponseRedirect(reverse('forum:index'))
    #     if form.is_valid():
    #         #TODO save
    #         return HttpResponseRedirect(reverse('forum:thread', form.id))
    #
    #     return render(request, self.template_name, self._get_context(form.id, form))