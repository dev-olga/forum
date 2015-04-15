
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import View
from forum import models
from forum import forms


class SubCategory(View):
    template_name = 'forum/sub-category.html'

    #TODO login check
    def get(self, request, id):
        return render(request, self.template_name, self._get_context(id, None, request.user))

    #TODO login check
    def post(self, request, id):
        form = forms.ThreadForm(request.POST)
        if not form:
            return HttpResponseRedirect(reverse('forum:index'))

        self._init_form(form, request.user)
        if form.is_valid():
            form.instance.sub_category = get_object_or_404(models.SubCategory, id=id)
            form.save()
            return HttpResponseRedirect(reverse('forum:thread', kwargs={'id': form.instance.id}))

        return render(request, self.template_name, self._get_context(id, form, request.user))

    def _get_context(self, id, form, user):
        subcategory = get_object_or_404(models.SubCategory, id=id)
        categories = models.Category.objects.all()

        if not form:
            form = forms.ThreadForm()
        self._init_form(form, user)

        return {'categories': categories, 'subcategory': subcategory, 'form': form}

    def _init_form(self, form, user):
        if user and user.is_authenticated():
            form.instance.user = user

    # def get(self, request, *args, **kwargs):
    #     subcategory = get_object_or_404(models.SubCategory, id=kwargs['pk'])
    #     categories = models.Category.objects.all()
    #     return render(request, self.template_name, {'categories': categories, 'subcategory': subcategory})


# class SubCategory(DetailView):
#     template_name = 'forum/sub-category.html'
#     queryset = models.SubCategory.objects.all()
#
#     def get_object(self):
#         object = super(SubCategory, self).get_object()
#         return object

    # def get_queryset(self):
    #     self.subcategory = get_object_or_404(models.SubCategory, id=self.kwargs['id'])
    #     return self.subcategory
    # def get(self, request, *args, **kwargs):
    #     try:
    #         subcategory = get_object_or_404(SubCategory, id=kwargs['id'])
    #     except ObjectDoesNotExist:
    #         pass
    #     categories = Category.objects.all()
    #     return render(request, self.template_name, {'categories': categories, 'subcategory': subcategory})