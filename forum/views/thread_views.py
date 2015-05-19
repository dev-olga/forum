from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic import View
import datetime

from forum import forms
from forum import models
from forum.view_decorators.show_view import thread_login_required
from forum import mixins


class ThreadView(mixins.CategoriesContextMixin, View):

    template_name = 'forum/thread/thread.html'

    @method_decorator(thread_login_required)
    def dispatch(self, *args, **kwargs):
        return super(ThreadView, self).dispatch(*args, **kwargs)

    def get(self, request, id, reply_to_id=None):
        return render(request, self.template_name, self.get_context_data(
            id=id, form=None, user=request.user, reply_to=reply_to_id))

    def post(self, request, id, reply_to_id=None):
        form = forms.PostForm(request.user, request.POST, request.FILES)
        if not form:
            return HttpResponseRedirect(reverse('forum:index'))

        if form.is_valid():
            form.instance.thread = get_object_or_404(models.Thread, id=id)
            if reply_to_id:
                form.instance.parent_post = get_object_or_404(models.Post, id=reply_to_id)
            form.save()
            return HttpResponseRedirect(reverse('forum:thread', kwargs={'id': id}) + "#" + str(form.instance.id))

        return render(request, self.template_name, self.get_context_data(
            id=id, form=form, user=request.user, reply_to=reply_to_id))

    def get_context_data(self, id, form, user, reply_to):

        context = super(ThreadView, self).get_context_data()
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
        context['thread_loading_date'] = int(datetime.datetime.now().strftime("%s"))
        return context

# class ThreadView(BaseForumView):
#
#     template_name = 'forum/thread/thread.html'
#
#     @method_decorator(thread_login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(ThreadView, self).dispatch(*args, **kwargs)
#
#     def get(self, request, id, reply_to_id=None):
#         return render(request, self.template_name, self._get_context(
#             id=id, form=None, user=request.user, reply_to=reply_to_id))
#
#     def post(self, request, id, reply_to_id=None):
#         form = forms.PostForm(request.user, request.POST, request.FILES)
#         if not form:
#             return HttpResponseRedirect(reverse('forum:index'))
#
#         if form.is_valid():
#             form.instance.thread = get_object_or_404(models.Thread, id=id)
#             if reply_to_id:
#                 form.instance.parent_post = get_object_or_404(models.Post, id=reply_to_id)
#             form.save()
#             return HttpResponseRedirect(reverse('forum:thread', kwargs={'id': id}) + "#" + str(form.instance.id))
#
#         return render(request, self.template_name, self._get_context(
#             id=id, form=form, user=request.user, reply_to=reply_to_id))
#
#     def _get_context(self, id, form, user, reply_to):
#
#         context = super(ThreadView, self)._get_context()
#         thread = get_object_or_404(models.Thread, id=id)
#
#         if reply_to:
#             post = get_object_or_404(models.Post, id=reply_to)
#             if post.thread != thread:
#                 raise Http404('Post {0} for thread {1} not found'.format(reply_to, id))
#
#         if not form:
#             form = forms.PostForm(user)
#
#         context['thread'] = thread
#         context['form'] = form
#         context['reply_to'] = reply_to
#         context['thread_loading_date'] = int(datetime.datetime.now().strftime("%s"))
#         return context


class CheckNewPostsView(View):

    def get(self, request, id, last_loaded):
        last_date = datetime.datetime.fromtimestamp(float(last_loaded))
        new_posts = len(models.Post.objects.filter(thread__id=id, date__gte=last_date)[:1]) > 0
        return JsonResponse({'new_posts': new_posts}, status=200)



