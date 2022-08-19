"""
ecommerce URL Configuration
"""
from django.contrib import admin
from django.urls import path

from ecommerce.drf.views import CategoryList

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/inventory/category/all/", CategoryList.as_view()),
]
