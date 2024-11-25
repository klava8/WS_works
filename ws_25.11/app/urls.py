from django.urls import path, include
from .views import MainPage, CustomLoginView

urlpatterns = [
    path("", MainPage.as_view(), name="home"),
    path("access/", CustomLoginView.as_view(), name="access"),
    
]