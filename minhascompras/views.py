from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ItemSerializer

from .models import Item

# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer