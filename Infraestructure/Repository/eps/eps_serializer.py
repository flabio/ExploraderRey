from app.eps.models import  Eps
from rest_framework import  serializers
class eps_serializer(serializers.ModelSerializer):
    class Meta:
        model = Eps
        fields=['eps_id','nombre','estado','created','modified']