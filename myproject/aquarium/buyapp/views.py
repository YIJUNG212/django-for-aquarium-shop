from django.shortcuts import render
from django.shortcuts import HttpResponse

from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET'])
def my_view(request):
    # your view code here
    pass

def redirect_to_https(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.is_secure():
            url = request.build_absolute_uri(request.get_full_path())
            secure_url = url.replace("http://", "https://")
            return redirect(secure_url)
        return view_func(request, *args, **kwargs)
    return wrapper
def index(request):
    return HttpResponse("test")