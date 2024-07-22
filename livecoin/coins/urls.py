from django.urls import path
from . import views
urlpatterns = [
    path('', views.login, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('coins', views.coins, name='coins'),
    path('profile', views.profile, name='profile'),
    path('downliners', views.downliners,name='downliners'),
    path('transactions', views.transactions,name='transactions'),
]