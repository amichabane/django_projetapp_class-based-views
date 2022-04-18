from django.urls import path

from django.contrib.auth.views import LogoutView
from .views import Login,Register


urlpatterns = [
    path('login/',Login.as_view(),name='login'),
    path('register/',Register.as_view(),name='register'),
    path('logout/',LogoutView.as_view(next_page ='login'),name='logout'),


]
