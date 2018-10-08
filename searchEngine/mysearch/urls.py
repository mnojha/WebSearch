from django.urls import path
from . import views

urlpatterns = [
	path('', views.indexView, name = "index"),
	path('<int:product_id>/', views.detail, name='detail'),
]