from rest_framework.serializers import ModelSerializer

from utils.models import House, IndustrialProperty

class HouseSerializer(ModelSerializer):
    class Meta:
        model = House
        fields = "__all__"

class IndustrialPropertySerializer(ModelSerializer):
    class Meta:
        model = IndustrialProperty
        fields = "__all__"
