from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth import login, authenticate
from .models import *
from django.contrib.auth.models import User

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user =requests.get('https://api/v1/user/register').json()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request , 'registration/registration_form.html', context)
    return render(request, 'registration/register.html')

def loginPage(request):
    if request.method == 'POST':
        emailAddress = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=emailAddress, password=password)
        user = request.get('https://api/v1/user/login').json()
        if user is not None:
            login(request, user)
            return redirect('')
        else:
            messages.info(request, 'Username or Password is incorrect for user - ' + username)
    context = {}
    return render(request, 'registration/login.html', context)

def home(request):
    
    return render(request, 'home.html')




# view functions below
def Dashboard(request):
    try:
        neighbourhood =requests.get('https://api/v1/neighbourhood/list_all').json()
        neighbourhood = neighbourhood[::-1]
    except:
        neighbourhood = []
    context = {
        'neighbourhood': neighbourhood,
    }
    return render(request, 'dashboard.html', context)


# creating neighbourhood
def create_neighbourhood(request):
    try:
        all_neighbourhood = requests.get('http://api/v1/neighbourhood/create').json() #list all endpoints
        all_neighbourhood = []
    if request.method =='POST':
        form = NeighbourHoodForm(request.POST)
        data={}
        if form.is_valid():
            data=form.data  
            post_neighbourhood = json.dumps(data)
            requests.post('https://api/v1/neighbourhood/create', post_neighbourhood) # use create endpoint
            print(post_neighbourhood) 
            messages.success(request, 'Neighbourhood was added Successfully')
            return redirect('neighbourhood')
        else:
            form = NeighbourHoodForm()
    context = {
        'form':form, 
        'all_neighbourhood': all_neighbourhood
    }
    return render(request, 'residents/neigbourhood_add.html', context)


# creating single neigbourhood
def single_neighbourhood(request, neighbourhood_id):
    singleNeighbourhood = requests.get('http://..../{:s}'.format(neighbourhood_id)).json()
    singleBusiness = requests.get('http://..../{:s}'.format(neighbourhood_id)).json()

    business = Business.objects.filter(neighbourhood=singleNeighbourhood)
    new_post = Post.objects.filter(singleNeighbourhood=singleNeighbourhood)
    new_post = new_post[::-1]
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        data = {}
        if form.is_valid():
            data = form.data
            post_neighbourhood = json.dumps(data)
            requests.post('https://api/v1/neighbourhood/create', post_neighbourhood)
            print(post_neighbourhood)
            messages.success(request, 'New Neighbourhood was added Successfully')
            return redirect('neighbourhood')
        else:
            form = BusinessForm()
    context = {
        'singleNeighbourhood': singleNeighbourhood,
        'business': business,
        'form': form,
        'new_post': new_post
    }
    return render(request, 'eachhood.html', context)


# creating posts
def create_post(request, neighbourhood_id):
    hood = NeighbourHood.objects.get(id=hood_id) # without endpoint
    hood = requests.get('http://..../{:s}'.format(neighbourhood_id)).json()
     if request.method == 'POST':
            form = PostForm(request.POST)
        data = {}
        if form.is_valid():
            data = form.data
            post = json.dumps(data)
            requests.post('https://new', post)
            print(post)
            messages.success(request, 'New post was added Successfully')
            return redirect('post')
        else:
            form = PostForm()
    context = {
        'form': form,
        'hood': hood
    }
    return render(request, 'post.html', context)


# ======Business View
# creating Businesses
def create_business(request, business_id):
    business = Business.objects.get(id=business_id) # without endpoint
    business = requests.get('http://api/v1/business/create{:s}'.format(business_id)).json()
     if request.method == 'POST':
            form = PostForm(request.POST)
        data = {}
        if form.is_valid():
            data = form.data
            post = json.dumps(data)
            requests.post('https://api/v1/business/list_all', post)
            print(post)
            messages.success(request, 'New post was added Successfully')
            return redirect('post')
        else:
            form = PostForm()
    context = {
        'form': form,
        'hood': hood
    }
    return render(request, 'Bizz/New_bizz.html', context)
