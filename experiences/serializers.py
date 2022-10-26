from rest_framework import serializers

from categories.serializers import CategorySerializer
from experiences.models import Perk, Experience
from users.serializers import TinyUserSerializer


class PerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    host = TinyUserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    perks = PerkSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = "__all__"
