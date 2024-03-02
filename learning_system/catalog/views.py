from django.db.models import Count, ExpressionWrapper, F, FloatField, Value
from rest_framework import generics
from .models import Product
from django.utils import timezone
from .serializers import ProductSerializer, ProductStatisticSerializer
from django.db.models import F, ExpressionWrapper, FloatField, Value
from django.contrib.auth.models import User
from django.db.models import Count


# Create your views here.


class AvailableProductsListView(generics.ListAPIView):
    queryset = Product.objects.filter(datetime_start__lte=timezone.now()).annotate(
        lessons_count=Count('lesson'))

    serializer_class = ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    total_users = User.objects.count()

    queryset = Product.objects.annotate(
        num_students=Count('group__students', distinct=True),
        total_groups=Count('group', distinct=True),
        avg_group_fill=ExpressionWrapper(
            (Count('group__students', distinct=True) * 100) / (
                F('max_size_group') * F('total_groups')),
            output_field=FloatField()
        ),
        acquisition_percentage=ExpressionWrapper(
            (Count('accesses', distinct=True) * 100) / Value(
                total_users, output_field=FloatField()),
            output_field=FloatField()
        )
    ).distinct()
    serializer_class = ProductStatisticSerializer
