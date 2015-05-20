from django.views import generic
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator

from forum import forms
from forum import models
from forum import mixins
from forum.view_decorators.show_view import admin_login_required


class UpdatePostView(mixins.AjaxResponseMixin, mixins.ModalDialogMixin, generic.UpdateView):
    template_name = 'forum/thread/post_update.html'
    template_name_suffix = ""
    form_class = forms.PostUpdateForm
    model = models.Post

    @method_decorator(admin_login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdatePostView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('forum:thread', kwargs={'id': self.get_object().thread.id})

    def form_valid(self, form):
        return super(UpdatePostView, self).form_valid(form)

    def get_context_data(self, **kwargs):

        context = super(UpdatePostView, self).get_context_data(**kwargs)
        context['action'] = reverse('forum:update_post', kwargs={'pk': self.get_object().id})

        return context


class DeletePostView(generic.DeleteView):
    model = models.Post

    def get_success_url(self):
        return reverse('forum:thread', kwargs={'id': self.get_object().thread.id})