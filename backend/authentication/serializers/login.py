from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

CustomUser = get_user_model()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        min_length=4,
        max_length=128,
        required=True,
    )
    password = serializers.CharField(
        min_length=8,
        max_length=128,
        required=True,
        write_only=True,
    )

    def validate(self, attrs):
        user = authenticate(**attrs)

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

    def get_tokens(self, user):
        tokens = RefreshToken.for_user(user)
        refresh = str(tokens)
        access = str(tokens.access_token)
        data = {
            "refresh": refresh,
            "access": access
        }
        return data

    def create(self, validated_data):
        return validated_data['user']
