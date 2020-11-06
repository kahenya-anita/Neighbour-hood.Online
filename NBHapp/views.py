from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth import login, authenticate
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm


@unauthenticated_user
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

# =========== Login
@unauthenticated_user
def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login (request, user)
            return redirect('hood')
        else:
            message.info(request, 'Username Or Password is incorrect')    
    
    context = {}
    return render(request, 'registration/login.html', context)

# ============ Logout user
def logoutUser(request):
    logout(request)
    return redirect('login')

# ============ Profile page
def userPage(request):
    context = {}
    return render(request, 'profile.html', context)

# ============ Home Page
def home(request):
    return render(request, 'home.html')

# ============ View for list of neighbour hoods to display
@login_required(login_url='login')
def hood(request):
    neighbourhoods = Neighbourhood.objects.all()
    return render(request, 'hood.html', {'neighbourhoods':neighbourhoods} )


# =========== For Each neighbour hood
@login_required
def estate(request, id):
    neighbourhoods = Neighbourhood.objects.get(id =id)
    businessa = Business.objects.get(id =id)
    hood = Neighbourhood.objects.get(id =id)

    context = {'hood': hood,'businessa':businessa, 'neighbourhoods':neighbourhoods}
    return render(request, 'eachhood.html', context)

#=========Creating a Neighbourhood
@login_required
def create_hood(request):
    userX = request.user
    
    if request.method =="POST":
        form = NeighbourHoodForm(request.POST, request.FILES)
        form_s = HoodForm(request.POST, request.FILES)
        
        if form_s.is_valid and form.is_valid():
            data_s = form_s.save()
            data = form.save(commit=False)
            data.user = userx
            data.hood = data_s
            data.save()
            return redirect('hood')
        else:
            return False
    return render(request, 'hood.html', 'form':NeighbourHoodForm, 'form_s':HoodForm)
    

# creating single neigbourhood
# @login_required(login_url='registration/login/')
# def single_neighbourhood(request, neighbourhood_id):
#     singleNeighbourhood = requests.get('http://api/v1/neighbourhood/find'.format(neighbourhood_id)).json()
#     singleBusiness = requests.get('http://api/v1/business/list_all').json()

#     business = Business.objects.filter(neighbourhood=singleNeighbourhood)
#     new_post = Post.objects.filter(singleNeighbourhood=singleNeighbourhood)
#     new_post = new_post[::-1]
#     if request.method == 'POST':
#         form = BusinessForm(request.POST)
#         data = {}
#         if form.is_valid():
#             data = form.data
#             post_neighbourhood = json.dumps(data)
#             requests.post('https://api/v1/neighbourhood/create', post_neighbourhood)
#             print(post_neighbourhood)
#             messages.success(request, 'New Neighbourhood was added Successfully')
#             return redirect('neighbourhood')
#         else:
#             form = BusinessForm()
#     context = {
#         'singleNeighbourhood': singleNeighbourhood,
#         'business': business,
#         'form': form,
#         'new_post': new_post
#     }
#     return render(request, 'eachhood.html', context)

# @login_required(login_url='registration/login/')
# def Neighbourhood_Delete(request,user_id):
#     neighbourhood = requests.get('https://api/v1/neighbourhood/find'.format(neighbourhood_id)).json() 
#     print(neighbourhood) 
#     url ='https://api/v1/neighbourhood/delete' 
#     neigbourhood['neighbourhood_id']= neighbourhood_id;
#     post_data = json.dumps(user)
#     print("\n see which hood i want to delete \n" + post_data)
#     requests.Delete(url, post_data)
#     return HttpResponseRedirect('hood.html') 
#     context = {
#         'neighbourhood':neighbourHood
#     }


# #====POSTS
# # creating posts
# def create_post(request, neighbourhood_id):
#     hood = NeighbourHood.objects.get(id=hood_id) # without endpoint
#     hood = requests.get('http://..../{:s}'.format(neighbourhood_id)).json()
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         data = {}
#         if form.is_valid():
#             data = form.data
#             post = json.dumps(data)
#             requests.post('https://new', post)
#             print(post)
#             messages.success(request, 'New post was added Successfully')
#             return redirect('post')
#         else:
#             form = PostForm()
#     context = {
#         'form': form,
#         'hood': hood
#     }
#     return render(request, 'post.html', context)


# # ======Business View
# # creating Businesses
# @login_required(login_url='registration/login/')
# def create_business(request, business_id):
#     business = Business.objects.get(id=business_id) # without endpoint
#     business = requests.get('http://api/v1/business/create'.format(business_id)).json()
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         data = {}
#         if form.is_valid():
#             data = form.data
#             post = json.dumps(data)
#             requests.post('https://api/v1/business/find', post)
#             print(post)
#             messages.success(request, 'New business was added Successfully')
#             return redirect('post')
#         else:
#             form = PostForm()
#     context = {
#         'form': form,
#         'hood': hood
#     }
#     return render(request, 'Bizz/New_bizz.html', context)

# # update  business function
# @login_required(login_url='registration/login/')
# def Business_update(request,business_id):
#     business = requests.get('http://api/v1/business/find'.format(business_id)).json() 
#     url ='https://api/v1/business/update '
#     business['business_id']=business_id
#     post_data = json.dumps(user)
#     requests.post(url, post_data)
#     return HttpResponseRedirect('hood')
#     context = {
#         'business':business
#     }

# #Delete business function
# @login_required(login_url='registration/login/')
# def Business_Delete(request,user_id):
#     user = requests.get('https://api/v1/business/find'.format(business_id)).json() 
#     print(user) 
#     url ='https://api/v1/business/delete' 
#     user['user_id']= user_id;
#     post_data = json.dumps(user)
#     print("\n see who i want to delete \n" + post_data)
#     requests.Delete(url, post_data)
#     return HttpResponseRedirect('hood.html') 
#     context = {
#         'user':user
#     }


 
