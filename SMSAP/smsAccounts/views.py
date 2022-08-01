from django.shortcuts import render
from .serializers import profileSerializer
from rest_framework import viewsets
from .models import Profile
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = profileSerializer
    
    parser_classes = (MultiPartParser, FormParser)
    
    # permission_classes = [
    #                 permissions.IsAuthenticatedOrReadOnly]

