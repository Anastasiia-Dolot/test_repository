from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('posts/', views.NewsView.as_view(), name='posts'),
    path('posts/<int:pk>', views.NewsDetail.as_view(), name='post_detail'),
    path('add/', views.NewsAdd.as_view(), name='addnews'),
    path('posts/<int:pk>/change/', views.NewsUpdate.as_view(), name='change'),
    path('posts/<int:pk>/delete/', views.NewsDel.as_view(), name='delete')
]