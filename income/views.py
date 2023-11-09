from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,RetrieveUpdateDestroyAPIView)
from .serializers import IncomeSerializer
from rest_framework import permissions
from .models import Income
from .permissions import IsOwner
# Create your views here.

class IncomeListAPIView(ListCreateAPIView):
    serializer_class = IncomeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Income.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class IncomeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = IncomeSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Income.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)