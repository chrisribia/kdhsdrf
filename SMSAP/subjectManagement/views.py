from django.shortcuts import render
from rest_framework import viewsets
from . models import SubjectList, SubjectSelectionList
from .serializers import SubjectListSerializer, SubjectSelectionListSerializer

class SubjectListViewset(viewsets.ModelViewSet):
    queryset = SubjectList.objects.all()
    serializer_class = SubjectListSerializer


class SubjectSelectionListViewset(viewsets.ModelViewSet):
    queryset = SubjectSelectionList.objects.all()
    serializer_class = SubjectSelectionListSerializer
