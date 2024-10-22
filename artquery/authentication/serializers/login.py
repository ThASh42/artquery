from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

User = get_user_model()


class LoginSerializers(serializers.Serializer):
    id = serializers.UUIDField()  # noqa:A003

    def create(self, validate_data):
        return validate_data['user']

    def update(self, instane, validated_data):
        pass

    def validate(self, data):
        pass

        try:
            user = User.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise serializers.ValidationError('Invalid login credentials')

        return {'user': user}
