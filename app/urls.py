from django.urls import path
from .views import*

urlpatterns = [
    path("studentapi/", Studentapi.as_view(), name = "studentapi"),
]
