from rest_framework import serializers
from .models import Oquv_markaz, oqituvchi

class OquvmarkazSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oquv_markaz
        fields=('name', 'xonalar_soni')

class oqituvchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = oqituvchi
        fields=('ismi', 'tel_nomer')
