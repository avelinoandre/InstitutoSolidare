from django.urls import path
from institutoSolidare.views import index, admLogin, admMain

urlpatterns = [
    path("", index, name="index"),
    path("adm-login/", admLogin, name="admLogin"),
    path("adm-main/", admMain, name="admMain"),
]
