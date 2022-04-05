from rest_framework import serializers
from .models import Table1

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Table1
        fields=('id','productname','price')
