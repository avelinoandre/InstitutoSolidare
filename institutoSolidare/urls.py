from django.urls import path
from institutoSolidare.views import index

urlpatterns = [
    path("", index, name="index"),
]
