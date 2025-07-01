from django.shortcuts import render
from rest_framework.views import APIView
from accounts.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "User registered successfully"}, status=201)
        
class AuthView(APIView):
    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            refresh_token = serializer.validated_data['refresh_token']
            access_token = serializer.validated_data['access_token']

            res = Response(
                {
                "user" : {
                    "id" : user.username,
                    "name" : user.first_name,
                    "age" : user.age
                },
                "accessToken" : access_token,
                "refreshToken" : refresh_token
                },
                status=status.HTTP_200_OK
            )

            return res
        
class MyPageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {
            "id": user.username,
            "name": user.first_name,
            "age": user.age
        }
        return Response(data, status=status.HTTP_200_OK)

class TokenRefreshView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refreshToken', None)

        if not refresh_token:
            return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)

            return Response({
                "accessToken": access_token,
                "refreshToken": str(refresh)
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
