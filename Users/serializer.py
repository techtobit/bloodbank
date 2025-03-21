from rest_framework import serializers
from django.contrib.auth import get_user_model
User=get_user_model()
from rest_framework import permissions
from .models import Feedback, Report


class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields="__all__"
        
    def create(self, validated_data):
        user=User.objects.create_user(
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
            full_name=validated_data['full_name'],
            blood_group=validated_data['blood_group'],
            division=validated_data['division'],
            district=validated_data['district'],
            upazila=validated_data['upazila']

        )
        return user

class DonarListSerializer(serializers.ModelSerializer):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    class Meta:
        model=User
        exclude = ['password', 'is_staff', 'is_superuser', 'user_permissions', 'groups']  

class DonarProfileSerializer(serializers.ModelSerializer):
    permission_classes = [permissions.IsAuthenticated]
    class Meta:
        model=User
        exclude = ['password', 'is_staff', 'is_superuser', 'user_permissions', 'groups']  

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields="__all__"

class ReportSerializer(serializers.ModelSerializer):    
    class Meta:
        model=Report
        fields="__all__"

