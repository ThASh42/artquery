from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.tokens import RefreshToken

from ....models.users import CustomUser


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        label=_("Username"),
        required=True,
        max_length=150,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())],
    )
    first_name = serializers.CharField(
        label=_("First Name"),
        required=False,
        max_length=150,
    )
    last_name = serializers.CharField(
        label=_("Last Name"),
        required=False,
        max_length=150,
    )
    email = serializers.EmailField(
        label=_("Email"),
        required=True,
        max_length=254,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())],
    )
    password1 = serializers.CharField(
        label=_("Password"),
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(
        label=_("Confirm password"),
        write_only=True,
        required=True,
    )

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
        )
        read_only_fields = ("id",)

    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password1": "Password fields didn't match."}
            )
        return attrs

    def get_tokens(self, user):
        tokens = RefreshToken.for_user(user)
        refresh = str(tokens)
        access = str(tokens.access_token)
        data = {"refresh": refresh, "access": access}
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
        )

        user.set_password(validated_data["password1"])
        user.save()

        return user
