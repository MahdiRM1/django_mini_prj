from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
        
class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'user', 'description', 'is_done', 'priority', 'due_date','created_at', 'tags']
        read_only_fields = ['id', 'created_at', 'user']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
    #
    # def create(self, validated_data):
    #     return User.objects.create_user(
    #         username=validated_data['username'],
    #         email=validated_data.get('email', ''),
    #         password=validated_data['password']
    #     )