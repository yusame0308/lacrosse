from rest_framework import routers
from .views import PlayerViewSet, InjuryViewSet, StickViewSet, ShotViewSet, PostViewSet, MenuViewSet


router = routers.DefaultRouter()
router.register('players', PlayerViewSet)
router.register('injuries', InjuryViewSet)
router.register('sticks', StickViewSet)
router.register('shots', ShotViewSet)
router.register('posts', PostViewSet)
router.register('menus', MenuViewSet)
