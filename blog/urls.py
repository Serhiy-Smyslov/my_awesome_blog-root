from django.urls import path
from . import views

urlpatterns = [
    path('', views.showblog, name='showblog'),
    path('<int:blog_id>/', views.specific_blog, name='blog'),
]