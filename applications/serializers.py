from applications.models import Application
from rest_framework import serializers

class ApplicationSerializer(serializers.ModelSerializer):
    apikey = serializers.ReadOnlyField(source='key')
    class Meta:
        model = Application
        fields = ['name', 'apikey']
