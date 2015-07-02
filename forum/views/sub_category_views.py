from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import View

from forum import models
from forum import forms
from forum import mixins
from forum.view_decorators.show_view import sub_category_login_required


class SubCategoryView(mixins.CategoriesContextMixin, View):

    template_name = 'forum/sub_category/sub_category.html'

    @method_decorator(sub_category_login_required)
    def dispatch(self, *args, **kwargs):
        return super(SubCategoryView, self).dispatch(*args, **kwargs)

    def get(self, request, id):
        return render(request, self.template_name, self.get_context_data(id, None, request.user))

    def post(self, request, id):
        form = forms.ThreadForm(request.user, request.POST, request.FILES)
        if not form:
            return HttpResponseRedirect(reverse('forum:index'))

        if form.is_valid():
            form.instance.sub_category = get_object_or_404(models.SubCategory, id=id)
            form.save()
            return HttpResponseRedirect(reverse('forum:thread', kwargs={'id': form.instance.id}))

        return render(request, self.template_name, self.get_context_data(id, form, request.user))

    def get_context_data(self, id, form, user):
        context = super(SubCategoryView, self).get_context_data()
        context['sub_category'] = get_object_or_404(models.SubCategory, id=id)

        if not form:
            form = forms.ThreadForm(user)
        context['form'] = form
        return context

