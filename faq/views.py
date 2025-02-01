from rest_framework.generics import ListAPIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import FAQ
from .serializers import FAQSerializer

@method_decorator(cache_page(60*15), name='dispatch')
class FAQListView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_serializer_context(self):
        return {'lang': self.request.query_params.get('lang', 'en')}