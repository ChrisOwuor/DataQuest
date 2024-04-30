from django.urls import path

from .views import AddData

urlpatterns = [
    path("data/", AddData.as_view(), name="index"),
]
