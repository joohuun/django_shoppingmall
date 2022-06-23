from django.contrib import admin

from user.models import User as UserModel
from user.models import Hobby as HobbyModel
from user.models import Profile as ProfileModel


# Register your models here.
admin.site.register(UserModel)
admin.site.register(HobbyModel)
admin.site.register(ProfileModel)

