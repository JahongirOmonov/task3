from rest_framework import serializers
from .models import Oquv_markaz, oqituvchi

class OquvmarkazSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oquv_markaz
        fields=('name', 'xonalar_soni')

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(OquvmarkazSerializer, self).create(validated_data)

class oqituvchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = oqituvchi
        fields=('ismi', 'tel_nomer')

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(oqituvchiSerializer, self).create(validated_data)
