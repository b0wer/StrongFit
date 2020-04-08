from django.shortcuts import render
from .models import ivent, IventUserProfile_photo
from django.views.generic.base import View
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import create_ivent, get_ivent, refresh_ivent


class list_ivent(View):
    def get(self, request):
        ivents = ivent.objects.all()
        return render(request, 'ivent/index.html', {'ivents': ivents})


class detail_ivent(View):
    def get(self, request, pk):
        Ivent = ivent.objects.get(id=pk)
        IventUserProfils = Ivent.IventUserProfils.all()
        return render(request, 'ivent/detail_ivent.html', {'ivent': Ivent, 'IventUserProfils': IventUserProfils})


# REST
class create_ivent(generics.CreateAPIView):
    serializer_class = create_ivent


class get_ivent(generics.ListAPIView):
    serializer_class = get_ivent
    queryset = ivent.objects.all()


class refresh_ivent(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = refresh_ivent
    queryset = ivent.objects.all()
