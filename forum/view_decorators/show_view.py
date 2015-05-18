from django.utils.functional import wraps
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from forum.models import Thread, SubCategory


def thread_login_required(view):
    @wraps(view)
    def inner(request, id, *args, **kwargs):
        thread = get_object_or_404(Thread, id=id)
 
        if not show_category(thread.sub_category.category, request.user):
            raise PermissionDenied
 
        return view(request, id, *args, **kwargs)
 
    return inner


def sub_category_login_required(view):
    @wraps(view)
    def inner(request, id, *args, **kwargs):
        sub_category = get_object_or_404(SubCategory, id=id)

        if not show_category(sub_category.category, request.user):
            raise PermissionDenied

        return view(request, id, *args, **kwargs)

    return inner


def show_category(category, user):
    return not category.auth_only or (user.is_authenticated and user.is_active)


def admin_login_required(view):
    @wraps(view)
    def inner(request, id, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return view(request, id, *args, **kwargs)

    return inner