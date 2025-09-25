from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from tweets.views import home, LikeTweetView, CommentTweetView
from rest_framework import routers
from tweets.views import TweetViewSet

router = routers.DefaultRouter()
router.register(r'tweets', TweetViewSet, basename='tweet')

urlpatterns = [
    path("home/", home, name="home"),  # Rota de teste
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),  # Rotas de usuário
    path("api/", include(router.urls)),        # Rotas do feed e tweets
    path("api/tweets/<int:tweet_id>/like/", LikeTweetView.as_view(), name="like-tweet"),
    path("api/tweets/<int:tweet_id>/comment/", CommentTweetView.as_view(), name="comment-tweet"),
]

# Debug Toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

# Servir arquivos de mídia durante desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
