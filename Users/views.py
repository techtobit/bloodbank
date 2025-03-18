from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions
from Users.serializer import RegisterSerializer, DonarListSerializer


User=get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'একউন্ট তৈরি হয়েছে'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DonarListView(APIView):
    # uthentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
            usernames = User.objects.all()
            serializer= DonarListSerializer(usernames, many=True)
            return Response(serializer.data)