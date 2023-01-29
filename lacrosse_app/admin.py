from django.contrib import admin

from .models import Player, Injury, Stick, Shot, Post, Menu


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'grade',)


@admin.register(Injury)
class InjuryAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'body', 'status', 'date',)
    
    
@admin.register(Stick)
class StickAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'depth', 'string', 'end', 'ball', 'length', 'narrow', 'height',)
    
    
@admin.register(Shot)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'date', 'score', 'gb', 'bd', 'pc', 'shot_all', 'shot_goal', 'shot_in',)
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'content', 'date',)
    
    
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'content', 'date',)
