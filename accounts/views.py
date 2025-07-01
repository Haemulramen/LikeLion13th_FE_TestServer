from django.shortcuts import render
from rest_framework.views import APIView
from accounts.serializers import *
from rest_framework.response import Response

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "User registered successfully"}, status=201)