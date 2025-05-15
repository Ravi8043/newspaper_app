from django.urls import path
from .views import get_list_view,get_detail_view, post_create_view, post_edit_view, post_delete_view

urlpatterns = [
    path('',get_list_view,name='home'),
    path('detail/<int:pk>/',get_detail_view, name='detail'),
    path('create/',post_create_view, name='create'),
    path('edit/<int:id>/',post_edit_view, name='edit'),
    path('delete/<int:id>/',post_delete_view, name='delete'),
]