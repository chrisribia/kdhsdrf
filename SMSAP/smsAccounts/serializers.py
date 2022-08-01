from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model 
from .models import Profile
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ('id','email','name','password')


class profileSerializer(serializers.ModelSerializer):  
    REQUIRED_FIELDS = '__all__'
    class Meta:
        model = Profile
        fields = ('__all__')