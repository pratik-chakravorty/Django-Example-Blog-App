from django.urls import path
from .views import blog_detail_view, blog_list_view, blog_create_view, blog_update_view, blog_delete_view
urlpatterns = [
     path('', blog_list_view, name='blog-list'),
     path('create/', blog_create_view, name='blog-create'),
     path('<id>/', blog_detail_view, name='blog-detail'),
     path('<id>/update/', blog_update_view, name='blog-update'),
     path('<id>/delete/', blog_delete_view, name='blog-delete'),
]
