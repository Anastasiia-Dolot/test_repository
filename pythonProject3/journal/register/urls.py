from django.urls import path
from . import views
from django.contrib.auth import views as LoginViews

urlpatterns = [
    path('', views.register, name='reg'),
    path('login/', LoginViews.LoginView.as_view(template_name='register/login.html'), name='login'),
    path('logout/', LoginViews.LogoutView.as_view(template_name='register/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile')
]