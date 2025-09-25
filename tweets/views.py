from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Tweet, Like, Comment
from .serializers import TweetSerializer, LikeSerializer, CommentSerializer
from users.models import CustomUser, Follow

# Rota de teste /home/
def home(request):
    return HttpResponse("API do Twitter Clone está no ar 🚀")

# ViewSet para Tweets
class TweetViewSet(viewsets.ModelViewSet):
    serializer_class = TweetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retorna tweets apenas de usuários que o usuário logado segue
        user = self.request.user
        following_users = Follow.objects.filter(follower=user).values_list('following', flat=True)
        return Tweet.objects.filter(user__in=following_users).order_by('-created_at')

    def perform_create(self, serializer):
        # Ao criar um tweet, associa o usuário logado
        serializer.save(user=self.request.user)

# Curtir tweet
class LikeTweetView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, tweet_id):
        tweet = get_object_or_404(Tweet, id=tweet_id)
        like, created = Like.objects.get_or_create(user=request.user, tweet=tweet)
        if not created:
            like.delete()
            return Response({"detail": "Like removido."})
        return Response({"detail": "Tweet curtido."})

# Comentar tweet
class CommentTweetView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, tweet_id):
        tweet = get_object_or_404(Tweet, id=tweet_id)
        content = request.data.get("content")
        if not content:
            return Response({"detail": "Conteúdo do comentário é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)
        comment = Comment.objects.create(user=request.user, tweet=tweet, content=content)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
