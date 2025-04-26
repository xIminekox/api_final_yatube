from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, GroupViewSet
from .views import FollowViewSet, MyTokenObtainPairView
from .views import MyTokenRefreshView, MyTokenVerifyView


router_v1 = DefaultRouter()


router_v1.register('posts', PostViewSet)
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments')
router_v1.register('groups', GroupViewSet)
router_v1.register('follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/jwt/create/',
         MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/jwt/refresh/',
         MyTokenRefreshView.as_view(), name='token_refresh'),
    path('v1/jwt/verify/', MyTokenVerifyView.as_view(), name='token_verify'),
]
