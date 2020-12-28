from rest_framework import serializers
from .models import Iglesia

class IglesiaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Iglesia
		fields ='__all__'