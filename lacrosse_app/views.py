from rest_framework import viewsets
from .models import Player, Injury, Stick, Shot, Post, Menu
from .serializer import PlayerSerializer, InjurySerializer, StickSerializer, ShotSerializer, PostSerializer, MenuSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class InjuryViewSet(viewsets.ModelViewSet):
    queryset = Injury.objects.all()
    serializer_class = InjurySerializer
    # filter_fields = ('player')
    
    
class StickViewSet(viewsets.ModelViewSet):
    queryset = Stick.objects.all()
    serializer_class = StickSerializer
    
    
class ShotViewSet(viewsets.ModelViewSet):
    queryset = Shot.objects.all()
    serializer_class = ShotSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class PostListView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = (AllowAny, )


# class PostDetailView(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# class MenuListView(generics.ListAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer
#     permission_classes = (AllowAny, )


# class MenuDetailView(generics.RetrieveAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer