from django.db.models import Q
from aktuels.models import Aktuel, AktuelProducts
from rest_framework import generics

from .serializers import (
    AktuelModelSerializer,
    AktuelProductModelSerializer,
    AktuelSlugModelSerializer
    )


class AktuelListAPIView(generics.ListAPIView):
    queryset = Aktuel.objects.all()
    serializer_class = AktuelModelSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Aktuel.objects.all()
        return qs


class AktuelDetailAPIView(generics.ListAPIView):
    serializer_class = AktuelProductModelSerializer

    def get_queryset(self, *args, **kwargs):
        aktuel_id = self.kwargs.get("pk")
        qs = AktuelProducts.objects.filter(aktuel_id=aktuel_id)
        return qs