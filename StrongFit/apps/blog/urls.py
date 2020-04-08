from django.urls import path
from django.urls import include
from .views import PostDetail, index, refresh_Post, create_Post
from .parser import parsing

urlpatterns = [
    path('', index, name='posts_list_url'),
    path('<int:id>', PostDetail.as_view(), name='post_detail_url'),
    path('refresh/<int:pk>/', refresh_Post.as_view()),
    path('create/', create_Post.as_view()),
    path('parsing/', parsing),
]