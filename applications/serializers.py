from applications.models import Application
from rest_framework import serializers

class ApplicationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Application
        fields = ['name', 'owner']


class ApplicationKeySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    
    def create(self, validated_data):
        return Application.objects.create(**validated_data)