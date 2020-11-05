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
    path('create_neighbourhood/', views.create_neighbourhood, name = 'create_neighbourhood'),
    path('single_neighbourhood/', views.single_neighbourhood, name = 'single_neighbourhood'),
    path('create_business/', views.create_business, name = 'create_business')
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)