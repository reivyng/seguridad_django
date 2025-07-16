from django.urls import path
from api.controllers.views import UserListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
]
