from django.urls import path
from .views import *


app_name = 'i8vdYk'

urlpatterns = [
    path('', IndexView.as_view(), name='InsdPj'),
    path('docs/<int:pk>', DocsView.as_view(), name='jK1h3A'),
    path('docs/<int:pk>/reply', DocsReplyView.as_view(), name='Akd1he'),
]
