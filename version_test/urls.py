from django.urls import path
from .views import CreatePostAPIView, CustomUserCreate, ObtainTokenPairWithCustomUserView, RetrieveUpdateDeletePostAPIView

urlpatterns = [
    path('api/register/', CustomUserCreate.as_view(), name='register'),
    path('api/login/', ObtainTokenPairWithCustomUserView.as_view(), name='login'),
    path('posts/', CreatePostAPIView.as_view(), name='create_post'),
    path('posts/<int:pk>/', RetrieveUpdateDeletePostAPIView.as_view(), name='retrieve_update_delete_post'),
]
