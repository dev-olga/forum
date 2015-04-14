from django.shortcuts import render
from django.views.generic import View


class Register(View):
    template_name = 'forum/register.html'

    def get(self, request):
        # <view logic>
        return render(request, self.template_name)