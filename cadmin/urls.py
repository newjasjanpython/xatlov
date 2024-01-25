from .views import *
from django.urls import path

app_name = "oR6PcG"


urlpatterns = [
    path('', IndexView.as_view(), name='oTcygr'),
    path('login/', LoginView.as_view(), name="Osjn1j"),
    path('list-problems/', ListProblems.as_view(), name="nJ2jar"),
    path('update-date/', UpdateDateView.as_view(), name="jkm2Na"),
    path('by-organization/', ByOrganizationsView.as_view(), name="lma31s"),
]
