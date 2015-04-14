from django.shortcuts import render
from django.views.generic import View


class Login(View):
    template_name = 'forum/login.html'

    def get(self, request):
        # <view logic>
        return render(request, self.template_name)