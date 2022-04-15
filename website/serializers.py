from rest_framework import serializers
from .models import Ai1


class Ai1Serial(serializers.ModelSerializer):
    class Meta:
        model = Ai1
        fields = ('id', 'current', 'sts')
