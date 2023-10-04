from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('', views.blog,name='blog'),
    path('<int:num>/', views.post_details,name='post_detail'),
    path('author/<str:auth>/', views.blog,name='author'),
    path('category/<str:cat>/', views.blog,name='category'),
    path('search/', views.search,name='search'),
    path('test/', views.test,name='test'),
]
