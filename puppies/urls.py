from django.urls import path
from . import views
from .views import signup, CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    
    path('', views.home, name='home'),
    path('add/', views.add_puppy, name='add_puppy'),
    path('list/', views.list_puppies, name='puppy_list'),
    path('signup/', views.signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
     path('search/', views.live_search, name='live_search'),
]
