from django.urls import path
from django.urls import include
from . import views

app_name = 'ivent'

urlpatterns = [
    path('', views.list_ivent.as_view()),
    path('<int:pk>/', views.detail_ivent.as_view()),
    path('create/', views.create_ivent.as_view()),
    path('get/', views.get_ivent.as_view()),
    path('refresh/<int:pk>/', views.refresh_ivent.as_view()),
    ] 