from django.urls import path
from accounts.views import UserDetailView

urlpatterns = [
    path('', UserDetailView.as_view(), name='user-detail'),
]
