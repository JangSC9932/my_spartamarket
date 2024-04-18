from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/change_password/', views.change_password, name='change_password'),
    path('profile/delete/', views.profile_delete, name='profile_delete'),
    path('profile/follow/<str:username>', views.profile_follow, name='profile_follow'),
    path('profile/unfollow/<str:username>', views.profile_unfollow, name='profile_unfollow'),
]