from rest_framework.generics import RetrieveAPIView, get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


from item.serializers import ItemSerializer

from item.models import Item

from item.service import create_checkout_session, create_product


class GetSessionAPIView(APIView):

    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        product = create_checkout_session(item)

        return Response({
            'item': item.__str__(),
            # 'url': price,
            'prod': product
        })


class ItemDetailAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'item_page.html'

    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        return Response({'item': item})
