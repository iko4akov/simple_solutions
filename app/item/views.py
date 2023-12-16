import stripe
from rest_framework.generics import RetrieveAPIView

from config.settings import STRIPE_SECRETE_KEY

from item.serializers import ItemSerializer

from item.models import Item

stripe.api_key = STRIPE_SECRETE_KEY

class GetSessionAPIView(RetrieveAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
