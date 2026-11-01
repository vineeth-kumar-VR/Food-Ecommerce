from django.urls import path
from . import views
urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("restaurants/", views.home_view, name="home"),
    path("logout/", views.logout_view, name="logout")
]
