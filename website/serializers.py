from rest_framework import serializers
from .models import Ai1, Ai2


class Ai1Serial(serializers.ModelSerializer):
    class Meta:
        model = Ai1
        fields = ('id', 'current', 'sts')


class Ai2Serial(serializers.ModelSerializer):
    class Meta:
        model = Ai2
        fields = ('id', 'current', 'sts')
