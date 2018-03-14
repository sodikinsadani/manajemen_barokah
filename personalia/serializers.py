from rest_framework import serializers
from personalia.models import Individu

class IndividuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individu
        fields = '__all__'