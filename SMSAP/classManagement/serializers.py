from rest_framework import serializers
from . models import ClassList, ClassMembersDetails




class ClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ClassList
        fields = ('ClassNames','Teacher')

class ClassMembersDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ClassMembersDetails
        fields = ('ClassLevelName','StudentReg')



 