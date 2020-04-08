from django.shortcuts import render
from .models import Post
from django.views.generic import View
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import refresh_Post, create_Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context= {'posts': posts,})

#def post_detail(request, id, slug):
#    post = Post.objects.get(id=id)
#    return render(request, 'blog/post_detail.html', context={'post': post})

class PostDetail(View):
    def get(selg, request, id):
        post = Post.objects.get(id__iexact=id)
        return render(request, 'blog/post_detail.html', context={'post': post})

class refresh_Post(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = refresh_Post
    queryset = Post.objects.all()  

class create_Post(generics.CreateAPIView):
    serializer_class = create_Post 