from app.patrulla.models import Patrulla
from rest_framework import  serializers

class patrulla_serializer(serializers.ModelSerializer):
    class Meta:
        model = Patrulla
        fields ='__all__'
        depth=1