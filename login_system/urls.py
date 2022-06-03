from django.urls import path, include
from .views import home_view, register_view, login_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_view, name='home_page'),
    path('register/', register_view, name='register_page'),
    path('login/', login_view, name='login_page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login_system/logout.html'), name='logout_page')
]
