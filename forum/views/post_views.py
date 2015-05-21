from django.views import generic
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator

from forum import forms
from forum import models
from forum import mixins
from forum.view_decorators.show_view import admin_login_required


class PostUpdateView(mixins.AjaxFormMixin, mixins.ModalDialogMixin, generic.UpdateView):
    template_name = 'forum/thread/post_update.html'
    template_name_suffix = ""
    form_class = forms.PostUpdateForm
    model = models.Post

    @method_decorator(admin_login_required)
    def dispatch(self, *args, **kwargs):
        return super(PostUpdateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        next_key='next'
        if next_key in self.request.POST:
            next = self.request.POST[next_key]
        if not next:
            next = reverse('forum:thread', kwargs={'id': self.get_object().thread.id})
        return next

    def form_valid(self, form):
        return super(PostUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('forum:post_update', kwargs={'pk': self.get_object().id})
        context['next'] = self.request.META['HTTP_REFERER']
        return context


class PostDeleteView(generic.DeleteView):
    model = models.Post

    def get_success_url(self):
        return reverse('forum:thread', kwargs={'id': self.get_object().thread.id})