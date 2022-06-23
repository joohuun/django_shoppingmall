from ast import Pass
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

# Create your views here.



class UserView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        return Response({'message':'get method!!'})

    def post(self, request):    
        return Response({'message':'post method!!'}) 
    
    def put(self, request):
        return Response({'message':'put method!!'})
  