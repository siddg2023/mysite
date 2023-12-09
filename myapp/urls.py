from django.urls import path
from .views import signup, custom_login, profile_detail, edit_profile, create_profile
from .views import recruiter_signup, recruiter_login, recruiter_dashboard

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', custom_login, name='custom_login'),
    path('profile/<str:username>/', profile_detail, name='profile_detail'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('create_profile/', create_profile, name='create_profile'),
    path('recruiter/signup/', recruiter_signup, name='recruiter_signup'),
    path('recruiter/login/', recruiter_login, name='recruiter_login'),
    path('recruiter/dashboard/', recruiter_dashboard, name='recruiter_dashboard'),
]


