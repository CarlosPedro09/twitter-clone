from django.contrib import admin
from django.utils.html import format_html
from .models import CustomUser, Follow

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'avatar_tag')  # mostra avatar na lista
    search_fields = ('username', 'email')
    fields = ('username', 'email', 'full_name', 'bio', 'avatar', 'password', 'is_staff', 'is_active', 'avatar_tag')
    readonly_fields = ('avatar_tag', 'password')  # avatar_tag e senha não editáveis

    def avatar_tag(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" style="width: 50px; height:50px; object-fit: cover; border-radius:50%;" />', obj.avatar.url)
        return "-"
    avatar_tag.short_description = 'Avatar'

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'following')
