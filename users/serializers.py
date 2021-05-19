from django.db.models import fields
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from .models import Acc


class accSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    

    class Meta:
        model = Acc
        fields = '__all__'