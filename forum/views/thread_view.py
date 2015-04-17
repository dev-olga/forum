from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from forum import forms
from forum import models
from forum.views.base_forum_view import BaseForumView


class ThreadView(BaseForumView):

    template_name = 'forum/thread.html'

    #TODO login check
    def get(self, request, id, reply_to=None):
        return render(request, self.template_name, self._get_context(
            id=id, form=None, user=request.user, reply_to=reply_to))

    #TODO login check
    def post(self, request, id, reply_to=None):
        form = forms.PostForm(request.user, request.POST, request.FILES)
        if not form:
            return HttpResponseRedirect(reverse('forum:index'))

        if form.is_valid():
            form.instance.thread = get_object_or_404(models.Thread, id=id)
            if reply_to:
                form.instance.parent_post = get_object_or_404(models.Post, id=reply_to)
            form.save()
            return HttpResponseRedirect(reverse('forum:thread', kwargs={'id': id}) + "#" + str(form.instance.id))

        return render(request, self.template_name, self._get_context(
            id=id, form=form, user=request.user, reply_to=reply_to))

    def _get_context(self, id, form, user, reply_to):

        context = super(ThreadView, self)._get_context()
        thread = get_object_or_404(models.Thread, id=id)

        if reply_to:
            post = get_object_or_404(models.Post, id=reply_to)
            if post.thread != thread:
                raise Http404('Post {0} for thread {1} not found'.format(reply_to, id))

        if not form:
            form = forms.PostForm(user)

        context['thread'] = thread
        context['form'] = form
        context['reply_to'] = reply_to
        return context