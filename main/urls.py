from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import *


app_name = "0hb7qY"


urlpatterns = [
    path('', IndexView.as_view(), name="MmejEU"),
    path('dev/api/problem/create/', csrf_exempt(ProblemCreateApi.as_view()), name="YNsH6t"),
    path('dev/api/problem/edit/', csrf_exempt(ProblemEditApi.as_view()), name="eKxUlD"),
    
    path('dev/api/member_inf/create/', csrf_exempt(MembersInForeignCreateApi.as_view()), name="RHtzUT"),
    path('dev/api/member_inf/edit/', csrf_exempt(MembersInForeignEditApi.as_view()), name="R9eOpx"),
    
    path('dev/api/member_in_note/create/', csrf_exempt(MembersInSomeNotebookCreateApi.as_view()), name="jMQUr1"),
    path('dev/api/member_in_note/edit/', csrf_exempt(MembersInSomeNotebookEditApi.as_view()), name="Z076ao"),
]
