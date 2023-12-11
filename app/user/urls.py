from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.apps import UserConfig
from user.views import (
    UsersListView, UsersRegistrationView,
    UsersRetrieveView, UsersUpdateView, UsersVerifyEmailView,
    UsersDestroyView,
)

app_name = UserConfig.name

urlpatterns = [
    path('', UsersListView.as_view(), name='user-list'),
    path('create/', UsersRegistrationView.as_view(), name='user-create'),
    path('<int:pk>/', UsersRetrieveView.as_view(), name='user-retrieve'),
    path('update/<int:pk>/', UsersUpdateView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UsersDestroyView.as_view(), name='user-destroy'),

    path(
        'verify_email/<uidb64>/<token>/',
        UsersVerifyEmailView.as_view(),
        name='verify-email'
    ),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
