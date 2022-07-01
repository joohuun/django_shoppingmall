from tkinter.tix import Tree
from rest_framework import serializers
import user
from user.models import User as UserModel
from user.models import Profile as ProfileModel
from user.models import Hobby as HobbyModel

class HobbySerializer(serializers.ModelSerializer):
    same_hobby_users = serializers.SerializerMethodField()
    def get_same_hobby_users(self, obj):
        user = self.context["request"].user
        print(user)
        
        # user_list = []
        # for profile in obj.profile_set.exclude(user=user): # obj=hobby, 취미모델에는 프로필객체가 없으므로 _set으로 가져옴
            # user_list.append(profile.user.username)
        # return user_list
        return [profile.user.username for profile in obj.profile_set.exclude(user=user)]
        
    class Meta:
        model = HobbyModel
        fields = ['name', "same_hobby_users"]
        
        
class ProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True)
    class Meta:
        model = ProfileModel
        fields = "__all__"
        
        
class UserSerializer(serializers.ModelSerializer):
    profile_set = ProfileSerializer(many=True)
    # profile_set = serializers.SerializerMethodField()
    # def get_profile_set(self, obj):
    #     user = self.context["request"].user
    #     print(user)
    #     retu
    
    class Meta:
        model = UserModel
        # fiedls = '__all__'
        fields = ["email", "username", "join_date", "date_of_birth", "profile_set"]
        

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
        
    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        pw = user.password
        user.set_password(pw)
        user.save()
        return user
    
    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)
        pw = user.password
        user.set_password(pw)
        user.save()
        return user