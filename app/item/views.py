from rest_framework.generics import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


from item.models import Item
from item.service import create_checkout_session, create_product

from config.settings import STRIPE_PUBLIC_KEY


class GetSessionAPIView(APIView):
    @staticmethod
    def get(request, pk: int) -> Response:
        item = get_object_or_404(Item, id=pk)
        checkout_session_id = create_checkout_session(item)

        return Response({
            'checkout_session_id': checkout_session_id,
        })


class ItemDetailAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'item_page.html'

    @staticmethod
    def get(request, pk):
        context = {
            "stripe_public_key": STRIPE_PUBLIC_KEY,
        }
        item = get_object_or_404(Item, id=pk)

        return Response({'item': item, 'context': context})
