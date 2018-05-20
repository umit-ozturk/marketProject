from django.db.models import Q
from aktuels.models import Aktuel


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
	queryset = Aktuel.objects.all()
	serializer_class = AktuelModelDetailSerializer

	def get_queryset(self, *args, **kwargs):
		aktuel_slug = self.kwargs.get("slug")
		qs = Aktuel.objects.filter(slug=aktuel_slug)
		if qs.exists() and qs.count() == 1:
			return qs
		return None
