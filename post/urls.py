from django.urls import path
from post import views


urlpatterns = [
  path("", views.PostListView.as_view(), name="list"),
  path ("<int:pk>/", views.PostDetailView.as_view(), name="detail"), 
  path ("new/", views.PostCreateView.as_view(), name="new"),
]