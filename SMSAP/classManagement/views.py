from django.shortcuts import render
from rest_framework import viewsets
from .models import ClassList, ClassMembersDetails
from .serializers import ClassListSerializer, ClassMembersDetailsSerializer

class ClassListViewset(viewsets.ModelViewSet):
    queryset = ClassList.objects.all()
    serializer_class = ClassListSerializer


class ClassMembersDetailsViewset(viewsets.ModelViewSet):
    queryset = ClassMembersDetails.objects.all()
    serializer_class = ClassMembersDetailsSerializer


