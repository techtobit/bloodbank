from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
User=get_user_model()

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
            upazila=validated_data['upazila'],
        )
        return user

class DonarListSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    is_staff=serializers.CharField(write_only=True)
    is_superuser=serializers.CharField(write_only=True)
    user_permissions=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields="__all__"
        # fields=['phone_number', 'full_name', 'blood_group', 'division', 'district', 'upazila']
    def get(self, request):
        userList=serializers( many=False, queryset=User.objects.all())
        return userList