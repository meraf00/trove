from django.urls import path
from auth import views

app_name = 'auth'

urlpatterns = [
    path('oauth/complete/', views.authenticate_with_oauth, name='oauth'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]