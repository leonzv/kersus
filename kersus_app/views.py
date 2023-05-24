from rest_framework import viewsets
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import generics, permissions, status
from .models import Category, Participant
from .serializers import CategorySerializer, ParticipantSerializer
from rest_framework.permissions import AllowAny
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    
class ParticipantView(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [AllowAny]

def index(request):
    return render(request, 'index.html')



