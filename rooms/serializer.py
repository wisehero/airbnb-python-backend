from rest_framework.serializers import ModelSerializer

from rooms.models import Amenity


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"

