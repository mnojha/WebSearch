from django.urls import path
from . import views

urlpatterns = [
	path('', views.indexView, name = "index"),
	path('search', views.search, name='search'),
	path('signup', views.signup, name='signup')
]