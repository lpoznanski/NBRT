from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('add-post/', views.AddPostView.as_view(), name='add-post'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
]