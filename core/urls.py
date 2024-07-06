from django.contrib import admin
from django.urls import path
from app.views import list_movies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_movies, name='list_movies'),
]
