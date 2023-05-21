from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('createauthor', views.createauthor, name="createauthor"),
    path('author', views.author, name="author"),
    path('readauthor/<int:author_id>/', views.readauthor, name="readauthor"),
    path('deleteauthor/<int:author_id>/', views.deleteauthor, name="deleteauthor"),
    path('editauthor/<int:author_id>/', views.editauthor, name="editauthor"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

































