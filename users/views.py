from django.http import request
from django.shortcuts import render
from rest_framework.settings import import_from_string
from .models import Acc
from .serializers import * 
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerProfileReadOnly


class UsersProfileListAPIView(ListCreateAPIView):
    queryset = Acc.objects.all()
    serializer = accSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)



class UsersProfileDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Acc.objects.all()
    serializer = accSerializers
    permission_classes = [IsOwnerProfileReadOnly, IsAuthenticated]


# Create your views here.
