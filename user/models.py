import email
from random import choices
from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser



# Create your models here.
class UserManger(BaseUserManager):             
    def create_user(self, email, date_of_birth, password=None):
        """
        입력된 이메일, 생일, 비밀번호로 사용자를 저장하고 생성함
        """
        if not email:
            raise ValueError('이메일은 필수 값입니다.')
        
        user = self.model(
            email = self.normalize_email(email),
            date_of_birth=date_of_birth,   
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, date_of_birth, password=None):
        
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):    
    email = models.EmailField("이메일", max_length=130, unique=True)
    username = models.CharField("유저이름", max_length=50)
    join_date = models.DateField("가입일", auto_now_add=True)
    date_of_birth = models.DateField("생일", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    class Meta:
        db_table = "user"
        
    def __str__(self):
        return f"{self.email} / {self.username}"
    
    objects = UserManger()   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
       
class Hobby(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = '취미'
        
    def __str__(self):
        return self.name
    
    
    

GENDER_CHOICE = (
        ("남","남"),
        ("여","여")
    ) 
class Profile(models.Model):
    user = models.ForeignKey('user.User', verbose_name="유저", on_delete=models.CASCADE)
    hobby = models.ManyToManyField('user.Hobby', verbose_name="취미")
    introduction = models.TextField("자기소개")
    gender = models.CharField("성별", max_length=10, choices=GENDER_CHOICE)
    
    class Meta:
        db_table = '프로필'
        
    def __str__(self):
        return f"{self.user} / {self.gender}"
    
    
    
    
    
    
    
    