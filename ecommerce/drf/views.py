from django.shortcuts import render
from ecommerce.drf.serializer import CategorySerializer
from ecommerce.inventory.models import Category
from rest_framework.response import Response
from rest_framework.views import APIView


class CategoryList(APIView):
    """Return list of categories"""

    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
