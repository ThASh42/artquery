from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import (
    AuthenticationFailed,
    InvalidToken,
    TokenError,
)
from rest_framework_simplejwt.tokens import RefreshToken


class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        access_token = request.COOKIES.get("access_token")
        refresh_token = request.COOKIES.get("refresh_token")

        if not access_token and refresh_token:
            try:
                access_token = str(RefreshToken(refresh_token).access_token)
            except (InvalidToken, TokenError) as e:
                raise AuthenticationFailed(f"Invalid refresh token: {e}")
        elif not access_token:
            return None

        try:
            validated_token = self.get_validated_token(access_token)
            user = self.get_user(validated_token)
            return user, validated_token
        except (AuthenticationFailed, InvalidToken, TokenError) as e:
            raise AuthenticationFailed(f"Authentication failed: {e}")
