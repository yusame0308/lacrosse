from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from lacrosse_app.urls import router as lacrosse_app_router
# from lacrosse_app.views import PostListView, PostDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(lacrosse_app_router.urls)),
    # path('post_list/', PostListView.as_view(), name='post'),
    # path('post/<str:pk>/', PostDetailView.as_view(), name = 'post-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)