from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostDelete

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:id>/', PostDetail.as_view(), name='post-detail'),
    path('posts/', PostCreate.as_view(), name='post-create'),
    path('posts/<int:id>/delete/', PostDelete.as_view(), name='post-delete'),
    path('create/', views.create_post, name='create-post'),
]
