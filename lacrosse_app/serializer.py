from rest_framework import serializers

from .models import Player, Injury, Stick, Shot, Post, Menu


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'grade')


class InjurySerializer(serializers.ModelSerializer):
    # player = PlayerSerializer()
    
    class Meta:
        model = Injury
        fields = ('id', 'player', 'body', 'status', 'date')
        
        
class StickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stick
        fields = ('id', 'player', 'depth', 'string', 'end', 'ball', 'length', 'narrow', 'height')
        
        
class ShotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shot
        fields = ('id', 'player', 'date', 'score', 'gb', 'bd', 'pc', 'shot_all', 'shot_goal', 'shot_in')


class PostSerializer(serializers.ModelSerializer):
    # date = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Post
        # fields = ('id', 'title', 'image', 'content')
        fields = ('id', 'title', 'image', 'content', 'date')
        
        
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        # fields = ('id', 'title', 'image', 'content')
        fields = ('id', 'title', 'image', 'content', 'date')
