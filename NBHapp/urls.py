from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('register/logout/', views.logoutUser, name = 'logout'),
    
    path('', views.home, name = 'home'),
    
    path('hood/', views.hood, name = 'hood'),
    path('add_biz/', views.add_biz, name = 'add_biz'),
    #path('change_neighbourhood/<int:id>/',views.change_neighbourhood, name='change_neighborhood'),


    path('estate/<int:id>/', views.estate, name = 'each-hood'),
    

    path('userPage/<int:id>/', views.userPage, name = 'profile'),
    path('search/', views.search, name = 'search'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)