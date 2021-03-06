from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views import generic
import datetime

from forum import forms
from forum import models
from forum.view_decorators.show_view import thread_login_required
from forum import mixins
from forum.view_decorators.show_view import admin_login_required


class ThreadView(mixins.CategoriesContextMixin, generic.View):

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
        context['thread_loading_date'] = datetime.datetime.utcnow().strftime("%s.%f")
        return context


class CheckNewPostsView(generic.View):

    def get(self, request, id, last_loaded):
        last_date = datetime.datetime.fromtimestamp(float(last_loaded))
        new_posts = len(models.Post.objects.filter(thread__id=id, date__gte=last_date)[:1]) > 0
        return JsonResponse({'new_posts': new_posts}, status=200)


# Admin part

class ThreadUpdateView(mixins.AjaxFormMixin, mixins.ModalDialogMixin, generic.UpdateView):
    template_name = 'forum/thread/thread_update.html'
    template_name_suffix = ""
    form_class = forms.ThreadUpdateForm
    model = models.Thread

    @method_decorator(admin_login_required)
    def dispatch(self, *args, **kwargs):
        return super(ThreadUpdateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('forum:subcategory', kwargs={'id': self.get_object().sub_category.id})

    def get_context_data(self, **kwargs):
        context = super(ThreadUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('forum:thread_update', kwargs={'pk': self.get_object().id})
        return context


class ThreadDeleteView(mixins.AjaxDeleteMixin, mixins.ModalDialogMixin, generic.DeleteView):
    template_name = 'forum/thread/thread_delete.html'
    template_name_suffix = ""
    model = models.Thread

    @method_decorator(admin_login_required)
    def dispatch(self, *args, **kwargs):
        return super(ThreadDeleteView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('forum:subcategory', kwargs={'id': self.get_object().sub_category.id})

    def get_context_data(self, **kwargs):
        context = super(ThreadDeleteView, self).get_context_data(**kwargs)
        context['action'] = reverse('forum:thread_delete', kwargs={'pk': self.get_object().id})
        return context


class PostUpdateView(mixins.AjaxFormMixin, mixins.ModalDialogMixin, generic.UpdateView):
    template_name = 'forum/thread/post_update.html'
    template_name_suffix = ""
    form_class = forms.PostUpdateForm
    model = models.Post

    @method_decorator(admin_login_required)
    def dispatch(self, *args, **kwargs):
        return super(PostUpdateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('forum:thread', kwargs={'id': self.get_object().thread.id})

    def form_valid(self, form):
        return super(PostUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('forum:post_update', kwargs={'pk': self.get_object().id})
        return context


class PostDeleteView(mixins.AjaxDeleteMixin, generic.DeleteView):
    template_name = 'forum/thread/post_delete.html'
    template_name_suffix = ""
    model = models.Post

    @method_decorator(admin_login_required)
    def dispatch(self, *args, **kwargs):
        return super(PostDeleteView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('forum:thread', kwargs={'id': self.get_object().thread.id})

    def get_context_data(self, **kwargs):
        context = super(PostDeleteView, self).get_context_data(**kwargs)
        context['action'] = reverse('forum:post_delete', kwargs={'pk': self.get_object().id})
        return context
