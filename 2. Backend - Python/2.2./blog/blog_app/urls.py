from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('add-post/', views.AddPostView.as_view(), name='add-post'),
    path('edit-post/<slug:slug>/', views.EditPostView.as_view(), name='edit-post'),
]