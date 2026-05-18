from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Advertisement

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = UserProfile
        fields = [
            'uuid',
            'username',
            'display_name',
            'email',
            'phone_number',
            'bio',
            'profile_picture',
            'created_at',
        ]
        read_only_fields = [
            'uuid',
            'username',
            'email',
            'created_at',
        ]