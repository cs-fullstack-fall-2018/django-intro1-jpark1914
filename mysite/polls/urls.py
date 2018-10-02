from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('language/', views.language),
    path('system/',views.system),
    path('ide/', views.ide)
]