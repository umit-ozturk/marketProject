from django.db.models import Q
from aktuels.models import Aktuel, AktuelProducts


from rest_framework import generics
from rest_framework.views import APIView


from .serializers import (
	AktuelModelSerializer,
	AktuelModelDetailSerializer
	)


class AktuelListAPIView(generics.ListAPIView):
	queryset = Aktuel.objects.all()
	serializer_class = AktuelModelSerializer

	def get_queryset(self, *args, **kwargs):
		qs = Aktuel.objects.all()
		return qs

class AktuelDetailAPIView(generics.ListAPIView):
	serializer_class = AktuelModelDetailSerializer

	def get_queryset(self, *args, **kwargs):
		aktuel_id = self.kwargs.get("pk")
		qs = AktuelProducts.objects.filter(aktuel=aktuel_id)
		query = self.request.GET.get("q")
		if query:
			qs = qs.filter(
				Q(price__range=query)
				).distinct()
		return qs