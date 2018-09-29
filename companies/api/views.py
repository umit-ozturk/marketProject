from companies.models import Company
from companies.api.serializers import CompanyDisplaySerializer


from rest_framework import generics


class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDisplaySerializer

    def get_queryset(self, *args, **kwargs):
        qs = Company.objects.filter(level=0)
        return qs
