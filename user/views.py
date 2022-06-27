import profile
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, viewsets, status
from user.models import User as UserModel
from user.models import Profile as ProfileModel
from user.models import Hobby as HobbyModel
from user.serializers import SignupSerializer, UserSerializer

# Create your views here.


class UserView(APIView):
    permission_classes = [permissions.AllowAny]
    # 유저인증
    def get(self, request):
        # 로그인된 유저 조회(request.user)
        # print(dir(request.user))
        user = UserSerializer(request.user, context={"request": request}).data
        return Response(user, status=status.HTTP_200_OK)
        
        # # 전체 사용자 조회
        # all_user = UserModel.objects.all()
        # all_users = UserSerializer(all_user, many=True).data
        # return Response(all_users, status=status.HTTP_200_OK)
               
    # 회원가입
    def post(self, request):
        signup_serializer = SignupSerializer(data=request.data)
        if signup_serializer.is_valid():
            signup_serializer.save()   
            return Response({"가입완료"}, status=status.HTTP_200_OK)
        else:
            print(signup_serializer.errors)
            return Response({"가입실패"}, status=status.HTTP_400_BAD_REQUEST)
    
    # 회원 정보 수정
    def put(self, request, user_id):
        user = get_object_or_404(UserModel, id=user_id)
        user_serializer = UserSerializer(data=request.data, instance=user, partial=True)
        
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({f"{user} 님의 정보가 변경 되었습니다."})
        
        
    # 회원 정보 삭제
    def delete(self, request, user_id):
        user = get_object_or_404(UserModel, id=user_id)
        user.delete()
        return Response({f"{user} 님의 정보가 삭제 되었습니다"})
    


class UserAPIView(APIView):
    # 로그인
    def post(self, request):
        email = request.data.get('email','')
        password = request.data.get('password','')
        
        user = authenticate(request, email=email, password=password)
        
        if not user:
            return Response({'존재하지 않는 계정이거나 패스워드가 일치하지 않습니다'},
                             status=status.HTTP_401_UNAUTHORIZED)
            
        login(request, user)
        return Response({"로그인 성공"},
                        status=status.HTTP_200_OK)
    # 로그아웃   
    def delete(self, request):
        logout(request)
        return Response({"로그아웃 성공"})
        
        
        
    
    
