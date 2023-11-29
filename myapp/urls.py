from django.urls import path
from .views import signup, custom_login, profile_detail, edit_profile, create_profile

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', custom_login, name='custom_login'),
    path('profile/', profile_detail, name='profile_detail'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('create_profile/', create_profile, name='create_profile'),
]


