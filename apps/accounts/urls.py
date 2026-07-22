from django.urls import path
from .views.auth import login_view, register_view, logout_view 
from .views.dashboard import dashboard_view
from .views.profile import profile_view

urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("profile/", profile_view, name="profile"),
]