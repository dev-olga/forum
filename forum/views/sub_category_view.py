
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import View
from forum import models
from forum import forms


class SubCategoryView(View):
    template_name = 'forum/sub-category.html'

    #TODO login check
    def get(self, request, id):
        return render(request, self.template_name, self._get_context(id, None, request.user))

    #TODO login check
    def post(self, request, id):
        form = forms.ThreadForm(request.user, request.POST, request.FILES)
        if not form:
            return HttpResponseRedirect(reverse('forum:index'))

        if form.is_valid():
            form.instance.sub_category = get_object_or_404(models.SubCategory, id=id)
            form.save()
            return HttpResponseRedirect(reverse('forum:thread', kwargs={'id': form.instance.id}))

        return render(request, self.template_name, self._get_context(id, form, request.user))

    def _get_context(self, id, form, user):
        sub_category = get_object_or_404(models.SubCategory, id=id)
        categories = models.Category.objects.all()

        if not form:
            form = forms.ThreadForm(user)

        return {'categories': categories, 'sub_category': sub_category, 'form': form}

