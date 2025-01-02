from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

CustomUser = get_user_model()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError({
                "non_field_errors": [_("Invalid email or password.")]
            })
        if not user.is_active:
            raise serializers.ValidationError({
                "non_field_errors": [_("This account is inactive.")]
            })
        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        return validated_data['user']
