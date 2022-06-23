from rest_framework import serializers
from user.models import User as UserModel
from user.models import Profile as ProfileModel
from user.models import Hobby as HobbyModel

class HobbySerializer(serializers.Serializer):
    class Meta:
        model = HobbyModel
        fields = ['name']
        
        
class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = ProfileModel
        fields = 