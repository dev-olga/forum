from django.views.generic import View, UpdateView
from forum.view_decorators.show_view import admin_login_required

class EditPostView(UpdateView):
    template_name = 'forum/thread/post_update.html'
    template_name_suffix = ""
    # success_url = lazy(reverse, str)('forum:index')
    form_class = forms.PostUpdateForm
    model = models.Post

    @method_decorator(admin_login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditPostView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('forum:thread', kwargs={'id': self.get_object().thread.id})