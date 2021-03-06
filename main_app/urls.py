from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('posts/', views.PostList.as_view(), name="post_list"),
    path('post/add', views.PostCreate.as_view(), name="post_create"),
    path('upload/', views.image_upload_view),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('posts/<int:pk>/update', views.PostUpdate.as_view(), name="post_update"),
    path('posts/<int:pk>delete', views.PostDelete.as_view(), name="post_delete"),
    path('accounts/signup/', views.signup_view, name="signup"),
    path('user/<username>/', views.profile, name='profile'),
    path('albums/', views.albums_index, name='albums_index'),
    path('albums/<int:album_id>', views.albums_show, name='albums_show'),
    path('albums/create/', views.AlbumCreate.as_view(), name='albums_create'),
    path('albums/<int:pk>/update/', views.AlbumUpdate.as_view(), name='albums_update'),
    path('albums/<int:pk>/delete/', views.AlbumDelete.as_view(), name='albums_delete'),
]
