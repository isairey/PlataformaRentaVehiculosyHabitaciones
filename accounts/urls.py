from django.urls import path
from .views import RegisterView, RetrieveUserView, UpdateUserView

urlpatterns = [
    path('register', RegisterView.as_view(), name="register_user"),
    path('me', RetrieveUserView.as_view(), name="retrieve_user"),
    path('update', UpdateUserView.as_view({'put': 'update'}), name="update_user")
]
