from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forum import forms
from forum import models
from forum.views.base_forum_view import BaseForumView


class ThreadView(BaseForumView):

    template_name = 'forum/thread.html'

    #TODO login check
    def get(self, request, id, **kwargs):
        return render(request, self.template_name, self._get_context(id, None, request.user, 0))

    #TODO login check
    def post(self, request, id, **kwargs):
        form = forms.PostForm(request.user, request.POST, request.FILES)
        if not form:
            return HttpResponseRedirect(reverse('forum:index'))

        if form.is_valid():
            form.instance.thread = get_object_or_404(models.Thread, id=id)
            form.save()
            return HttpResponseRedirect(reverse('forum:thread', kwargs={'id': id}) + "#" + str(form.instance.id))

        return render(request, self.template_name, self._get_context(id, form, request.user, 0))

    def _get_context(self, id, form, user, post_id=None):
        context = super(ThreadView, self)._get_context()
        context['thread'] = get_object_or_404(models.Thread, id=id)

        if not form:
            form = forms.PostForm(user)

        form.instance.parent_post_id = post_id

        context['form'] = form
        return context