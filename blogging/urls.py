from django.urls import path

from .views import (home_page, timeline_page, create_post, 
    profile_page, handle_follow_request, update_like, add_comment)

urlpatterns = [
    path('', home_page, name='home-page'),
    path('timeline/', timeline_page, name='timeline-page'),
    path('create_post/', create_post, name='create-post'),
    path('profile/<int:user_id>/', profile_page, name='profile-page'),
    path(
        'handle_follow_request/<int:user_id>/', 
        handle_follow_request, 
        name='handle-follow-request'
    ),
    path('update_like/', update_like, name='update-like'),
    path('add_comment/<int:post_id>/', add_comment, name='add-comment'),
]