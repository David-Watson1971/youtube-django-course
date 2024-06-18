from django.contrib import admin
from django.urls import path
from movies import views

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('movies/', views.movies),
    path('movies/<int:id>', views.detail),
    path('movies/add', views.add),
    path('movies/delete/<int:id>', views.delete),
]
