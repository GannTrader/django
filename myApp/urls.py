from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCatagoryView, CatagoryView, CatagoryListView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_catagory/', AddCatagoryView.as_view(), name="add_catagory"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/delete/', DeletePostView.as_view(), name="delete_post"),
    path('catagory/<str:cats>/', CatagoryView, name="catagory"),
    path('catagory-list/', CatagoryListView, name="catagory-list"),
]
