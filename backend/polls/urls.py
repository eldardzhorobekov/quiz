from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PollList.as_view(), name='poll-list'),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework')
]