from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('loging/', views.loging, name='loging'),
    path('registration/', RegisterUser.as_view(), name='registration'), 
    path('plan/', views.plan, name='plan'),
    path('diary/', views.diary, name='diary'),
    path('accounts/logout/', views.logout_user, name='logout'),
    path('articles_list/', views.articles, name='articles'),
    path('plans_list/', views.plans, name='plans'),
    path('lists/', views.lists, name='lists'),
]