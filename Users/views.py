from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions
from Users.serializer import RegisterSerializer, LoginSerializer, DonarListSerializer, DonarProfileSerializer, FeedbackSerializer, ReportSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import authentication, permissions
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
User=get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'একউন্ট তৈরি হয়েছে'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data = self.request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            password = serializer.validated_data['password']
            check_user = User.objects.filter(phone_number=phone_number).exists()
            if not check_user:
                return Response({'error' : "উক্ত নাম্বারটি দ্বারা একাউন্ট তৈরি হয়নি !"},  status=status.HTTP_404_NOT_FOUND)
            user = authenticate(phone_number= phone_number, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request, user)
                return Response({'token' : token.key, 'user_id' : user.id})
            else:
                return Response({'error' : "পাসওয়ার্ড সঠিক নয়, লগইন ব্যর্থ হয়েছে !"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors)
class DonarListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = DonarListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['division', 'district', 'upazila', 'blood_group']
    
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


class FeedbackView(APIView):
    def post(self, request):
        serializer=FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'প্রতিক্রিয়া দেওয়া হয়েছে'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReportView(APIView):
    def post(self, request):
        serializer=ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'রিপোর্ট করা হয়েছে'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

