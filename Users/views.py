from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.http import Http404
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions
from Users.serializer import RegisterSerializer, DonarListSerializer, DonarProfileSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import authentication, permissions

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
            users = User.objects.all()
            serializer= DonarListSerializer(users, many=True)
            return Response(serializer.data)
        
# class DonarProfileView(APIView):
#     # uthentication_classes = [authentication.TokenAuthentication]
#     # permission_classes = [permissions.AllowAny]
#     def get_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404
#     def get(self, request, pk, format=None):
#             user =self.get_object(pk=pk)
#             serializer= DonarProfileSerializer(user, many=False)
#             return Response(serializer.data)
#     def put(self, request, pk, format=None):
#         user =self.get_object(pk=pk)
#         serializer= DonarProfileSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     def delete(self, pk):
#         user =self.get_object(pk=pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
class DonarProfileView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = DonarProfileSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




