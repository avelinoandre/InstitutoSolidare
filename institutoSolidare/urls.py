from django.urls import path
from institutoSolidare.views import index, admLogin

urlpatterns = [
    path("", index, name="index"),
    path("adm-login/", admLogin, name="admLogin")
]
