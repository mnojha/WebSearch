from django.urls import path
from . import views

urlpatterns = [
	path('', views.indexView, name = "index"),
	path('login/', views.user_login, name='login'),
	path('search', views.search, name='search'),
	path('signup', views.signup, name='signup')
]