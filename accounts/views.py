from django.shortcuts import render, get_object_or_404
from .serializers import ProfileSerializer, UserCreateSerializer
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.

class ProfileView(generics.ListCreateAPIView):
    http_method_names = ["get"]
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(username=user.username) 


class UserCreate(APIView):
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserCreateSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        email = request.data['email']
        request.data['username'] = email
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserUpdate(APIView):   
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserCreateSerializer(snippet)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserCreateSerializer(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    