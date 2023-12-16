from django.urls import path
from item.apps import ItemConfig

from item.views import GetSessionAPIView

app_name = ItemConfig.name

urlpatterns = [
    path('buy/<int:pk>/', GetSessionAPIView.as_view(), name='buy'),
]
