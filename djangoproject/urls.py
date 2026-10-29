from django.contrib import admin
from django.urls import path

from hello_world_app.views import book_catalog, home, media_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('media/<int:pk>/', media_detail, name='media_detail'),
    path('books/', book_catalog, name='book_catalog'),
]
