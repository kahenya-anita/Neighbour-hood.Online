from django.http import HttpResponse
from django.shortcuts import redirect

# A decorator is a function that takes in another funtion as a 
# parameter and lets us ad some functonality

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):# if user is authenticated take them to the homepage
        if request.user.is_authenticated:
            return redirect('hood')
        else:# If youre logged in then you wont be able to view the login or sign up page
            return view_func(request, *args, **kwargs)

    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
           
           
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorised to view this page')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'tenant':
            return redirect('hood')
        elif group == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')# <- return response here (possibly a redirect to login page?)

    return wrapper_function