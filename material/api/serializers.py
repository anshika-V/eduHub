from material.models import TestSeries, Test
from rest_framework import serializers


class TestSummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = ['id', 'title']


class TestSeriesSerializer(serializers.ModelSerializer):
    tests = TestSummarySerializer(many=True, read_only=True)

    class Meta:
        model = TestSeries
        fields = '__all__'
