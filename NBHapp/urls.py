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
    path('estate/', views.estate, name = 'each-hood'),
    


    path('profile/', views.userPage, name = 'user-page')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)