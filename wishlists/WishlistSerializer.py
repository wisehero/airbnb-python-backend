from rest_framework.serializers import ModelSerializer

from rooms.serializer import RoomListSerializer
from wishlists.models import Wishlist


class WishlistSerializer(ModelSerializer):
    rooms = RoomListSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Wishlist
        fields = (
            "pk",
            "name",
            "rooms",
        )
