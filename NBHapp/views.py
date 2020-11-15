from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect, Http404
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from . decorators import unauthenticated_user
from .forms import *


def register(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')


    context = {'form':form}
    return render(request, 'registration/register.html', context)


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login (request, user)
            return redirect('create_profile')
        else:
            messages.info(request, 'Username Or Password is incorrect')    
    
    context = {}
    return render(request, 'registration/login.html', context)


# ============ Logout user
@login_required
def logoutUser(request):
    logout(request)
    return redirect('login')

# ============ Profile page

@login_required
def EditProfile(request,username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user = user)
    form = EditProfileForm(instance=profile)
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = user
            data.hood = profile.hood
            data.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            form = EditProfileForm(instance=profile)
    legend = 'Edit Profile'
    return render(request, 'profile.html', {'legend':legend, 'form':EditProfileForm})

@login_required(login_url='register/login/')
def create_profile(request):
    title = "NHood"
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = CreateProfileForm()
    return render(request, 'create_profile.html', {"form": CreateProfileForm, "title": title})       




    
# ============ Home Page
@login_required(login_url='register/login/')
def home(request):
    return render(request, 'home.html')

# ============ View for list of neighbour hoods to display
@login_required(login_url='register/login/')
def hood(request):
    neighbourhoods = Neighbourhood.objects.all()
    return render(request, 'hood.html', {'neighbourhoods':neighbourhoods} )


# =========== For Each neighbour hood
@login_required(login_url='register/login/')
def estate(request, id):
    neighbourhoods = Neighbourhood.objects.get(id =id)
    #businessa = Business.objects.get(id =id)
    hood = Neighbourhood.objects.get(id =id)

    context = {'hood': hood, 'neighbourhoods':neighbourhoods}
    return render(request, 'eachhood.html', context)
    

 ## ===Add Bizz   
@login_required(login_url='register/login/')
def add_biz(request):
    user = User.objects.filter(id = request.user.id).first()
    profile = UserProfile.objects.filter(user = user).first()
    if request.method == 'POST':
        business_form = AddBusinessForm(request.POST)
        if business_form.is_valid():
            business = Business(name = request.POST['name'],owner = user,business_neighborhood = profile.neighborhood,email=request.POST['email'])
            business.save()
        return redirect('eachhood.html')
    else:
        business_form = AddBusinessForm()
    return render(request,'Bizz/New_biz.html',{'business_form':business_form})

## ==Change Hood
# @login_required
# def change_neighbourhood(request,neighbourhood_id):
#     profile = UserProfile.objects.filter(user = request.user).first()
#     neighbourhood = Neighbourhood.objects.get(id=id)
#     profile.hood = neighbourhood
#     profile.save()
#     return redirect(reverse('hood',args=[neighbourhood.id]))

## =====Search Bizz
def search(request):
    try:
        if 'business' in request.GET and request.GET['business']:
            search_term = request.GET.get('business')
            searched_business = Business.objects.get(name__icontains=search_term)
            return render(request,'search.html',{'searched_business':searched_business})
    except (ValueError,Business.DoesNotExist):
        message = "Oops! We couldn't find the business you're looking for."
        return render(request,'search.html',{'message':message})
    return render(request,'search.html',{'message':message,'searched_business':searched_business})

     






