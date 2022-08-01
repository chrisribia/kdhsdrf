from rest_framework import serializers
from .models import SubjectList, SubjectSelectionList




class SubjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model  = SubjectList
        fields = ('SubjectName',)

class SubjectSelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model  = SubjectSelectionList
        fields = ('Subject','StudentClass','StudentRegNumber',)


