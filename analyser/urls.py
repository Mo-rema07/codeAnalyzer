from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('code_snippet/', views.code_snippet, name='code_snippet'),
    path('upload/', views.upload_file, name='upload'),
]
