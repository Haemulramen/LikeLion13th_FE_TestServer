from django.shortcuts import render
from rest_framework.views import APIView
from accounts.serializers import *
from rest_framework.response import Response
from rest_framework import status

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
        return Response(serializer.errors, status=400)
