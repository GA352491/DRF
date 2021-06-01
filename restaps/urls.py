from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_movies/', views.add_movies, name='add_movies'),
    path('api-auth/', include('rest_framework.urls')),
]
