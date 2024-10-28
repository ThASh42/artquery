from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

CustomUser = get_user_model()


class LoginSerializers(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')

        user = authenticate(username=email, password=password)
        if not user:
            raise serializers.ValidationError(('Invalid email or password'))
        validated_data['user'] = user
        return user
