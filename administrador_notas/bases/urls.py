from django.urls import include, path
from admin_notas.bases.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('login/',auth_views.LoginView.as_view(template_name="bases/login.html"),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="bases/login.html"),name='logout'),
    path('register/',signup_view,name="register"),
]
