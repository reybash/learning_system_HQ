from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    lessons_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'datetime_start', 'max_size_group',
                  'min_size_group', 'user', 
                  'lessons_count']


class ProductStatisticSerializer(serializers.ModelSerializer):
    num_students = serializers.IntegerField()
    avg_group_fill = serializers.FloatField()
    acquisition_percentage = serializers.FloatField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'num_students',
                  'avg_group_fill',
                  'acquisition_percentage']
