from django.contrib import admin
from django.urls import path
from quoteapp.views import index, get_about_author

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about_author/<str:name>', get_about_author, name='about_author'),
]
