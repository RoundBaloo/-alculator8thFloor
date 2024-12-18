from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
import calculatorFactPlan.components.is_need_change_password as is_need_change_password
from datetime import datetime

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
        
        change_password = is_need_change_password.ChangePassword
        
        is_need_password_change = change_password.get_need_change_password(user)
        print(is_need_password_change)

        return Response({
            'refresh': str(refresh),
            'access': str(access),
            'role': role,
            'is_need_password_change': is_need_password_change,
        })