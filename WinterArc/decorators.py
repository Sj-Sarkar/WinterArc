# decorators.py
from django.http import HttpResponseForbidden

def superuser_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden("You are not authorized to view this page.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func
