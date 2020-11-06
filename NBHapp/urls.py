from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('register/logout/', views.logoutUser, name = 'logout'),
    
    path('', views.home, name = 'home'),
    path('user/', views.userPage, name = 'user-page'),
    path('hood/', views.hood, name = 'hood'),
    path('create_businee/', views.create_business, name = 'bizz'),

    path('estate/<int:id>/', views.estate, name = 'each-hood'),
    

    path('profile/', views.userPage, name = 'user-page')
    path('search/',views.search,name='search'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)