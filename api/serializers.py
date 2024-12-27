from rest_framework import serializers
from drfapp.models import Item


# used to identify structure of the model while in views is used to query the exact data
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'