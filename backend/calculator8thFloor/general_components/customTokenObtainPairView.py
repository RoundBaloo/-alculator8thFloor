from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        token_data = serializer.validated_data
        refresh = token_data.get('refresh')
        access = token_data.get('access')

        # Получаем пользователя из токена
        user = serializer.user

        # Добавляем информацию о роли пользователя
        role = "admin" if user.is_superuser else "user"

        return Response({
            'refresh': str(refresh),
            'access': str(access),
            'role': role,
        })