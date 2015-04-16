from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def logout_view(request, redirect_to=''):
    logout(request)
    if redirect_to:
        return redirect(redirect_to)
    return redirect(reverse('forum:index'))
