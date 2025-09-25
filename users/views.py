from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from .models import Follow

User = get_user_model()

# Cadastro de usuário com retorno do token
class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Cria token automaticamente
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "username": user.username,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Atualizar perfil (username e senha)
class ProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user
        username = request.data.get("username")
        password = request.data.get("password")

        if username:
            user.username = username
        if password:
            user.set_password(password)
        user.save()

        return Response({
            "detail": "Perfil atualizado com sucesso!",
            "username": user.username
        })

# Seguir / deixar de seguir usuários
class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        if user_to_follow == request.user:
            return Response({"detail": "Não pode seguir você mesmo."}, status=status.HTTP_400_BAD_REQUEST)

        follow_obj, created = Follow.objects.get_or_create(
            follower=request.user,
            following=user_to_follow
        )

        if not created:
            # Já seguia, então desfaz o follow
            follow_obj.delete()
            return Response({"detail": f"Você deixou de seguir {user_to_follow.username}"})

        return Response({"detail": f"Você está seguindo {user_to_follow.username}"})
