from django.shortcuts import render


from .models import Oquv_markaz, oqituvchi
from django.http import JsonResponse
from .serializer import OquvmarkazSerializer, oqituvchiSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class GetAllOquvMarkaz(generics.ListAPIView):
    queryset=Oquv_markaz.objects.all()
    serializer_class=OquvmarkazSerializer
    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user)
        return Oquv_markaz.objects.all()

class GetDetailOquvMarkaz(generics.RetrieveAPIView):
    queryset = Oquv_markaz.objects.all()
    serializer_class=OquvmarkazSerializer

class PostOquvMarkaz(generics.CreateAPIView):
    queryset=Oquv_markaz.objects.all()
    serializer_class=OquvmarkazSerializer

class PatchOquvMarkaz(generics.UpdateAPIView):
    queryset=Oquv_markaz.objects.all()
    serializer_class=OquvmarkazSerializer

class DeleteOquvMarkaz(generics.DestroyAPIView):
    queryset=Oquv_markaz.objects.all()
    serializer_class=OquvmarkazSerializer

class PostGetOquvMarkaz(generics.ListCreateAPIView):
    queryset=Oquv_markaz.objects.all()
    serializer_class=OquvmarkazSerializer

class AllFunctionOquvMarkaz(generics.RetrieveUpdateDestroyAPIView):
    queryset=Oquv_markaz.objects.all()
    serializer_class=OquvmarkazSerializer


class GetAllOqituvchi(generics.ListAPIView):
    queryset=oqituvchi.objects.all()
    serializer_class=oqituvchiSerializer
    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user)
        return oqituvchi.objects.all()

class GetDetailOqituvchi(generics.RetrieveAPIView):
    queryset = oqituvchi.objects.all()
    serializer_class=oqituvchiSerializer

class PostOqituvchi(generics.CreateAPIView):
    queryset=oqituvchi.objects.all()
    serializer_class=oqituvchiSerializer

class PatchOqituvchi(generics.UpdateAPIView):
    queryset=oqituvchi.objects.all()
    serializer_class=oqituvchiSerializer

class DeleteOqituvchi(generics.DestroyAPIView):
    queryset=oqituvchi.objects.all()
    serializer_class=oqituvchiSerializer

class PostGetOqituvchi(generics.ListCreateAPIView):
    queryset=oqituvchi.objects.all()
    serializer_class=oqituvchiSerializer

class AllFunctionOqituvchi(generics.RetrieveUpdateDestroyAPIView):
    queryset=oqituvchi.objects.all()
    serializer_class=oqituvchiSerializer
