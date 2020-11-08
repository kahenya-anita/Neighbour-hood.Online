from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from . decorators import unauthenticated_user


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
            messages.info(request, 'Username Or Password is incorrect')    
    
    context = {}
    return render(request, 'registration/login.html', context)


# ============ Logout user
def logoutUser(request):
    logout(request)
    return redirect('login')

# ============ Profile page
@login_required(login_url='register/login/')
def Profile(request, user_id):
    user = User.objects.get(id = user_id)
    profile = UserProfile.objects.filter(user = user).first()
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,instance=profile)
        if form.is_valid():
            profile.name = request.POST['name']
            profile.bio = request.POST['bio']
            profile.hood = request.POST['hood']
            profile.image = request.POST['image']

            profile.save()
        return redirect(reverse('profile',args=[user.id]))
    else:
        form = UpdateProfileForm(instance=profile)

    businesses = Business.objects.filter(owner = user).all()
    neighborhoods = Neighborhood.objects.all()

    return render(request,'profile.html',{'neighborhoods':neighborhoods,'businesses':businesses,'profile':profile,'form':form})


# ============ Home Page
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
    business = Business.objects.get(id =id)
    hood = Neighbourhood.objects.get(id =id)

    context = {'hood': hood, 'business':business, 'neighbourhoods':neighbourhoods}
    return render(request, 'eachhood.html', context)

#=========Creating a Neighbourhood
@login_required(login_url='register/login/')
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
    return render(request, 'hood.html', {'form':NeighbourHoodForm, 'form_s':HoodForm})
 
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


 
