from django.urls import path
from .views import *
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login', LoginView.as_view(template_name='login.html'), name='login_url'),
    path('logout', LogoutView.as_view(), name='logout_url'),

    path('all_users', TemplateView.as_view(template_name='users_page.html'), name='all_users_url'),
    path('user_posts/<int:user_id>', TemplateView.as_view(template_name='user_posts_page.html'), name='user_posts_url'),
    path('add_post', TemplateView.as_view(template_name='add_post_page.html'), name='add_post_url'),

    path('users_api', GetAllUsersApiView.as_view(), name='users_api'),
    path('user_posts_api/<int:user_id>', GetUserPostsApiView.as_view(), name='user_posts_api'),
    path('add_post_api', AddPostApiView.as_view(), name='add_post_api'),
    path('delete_post_api/<int:post_id>', DeletePostApiView.as_view(), name='delete_post_api'),
]
