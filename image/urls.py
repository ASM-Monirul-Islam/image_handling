from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name="home"),
	path('view_image/', views.view_image, name="view_image"),
	path('create_image/', views.create_image, name="create_image"),
] 
