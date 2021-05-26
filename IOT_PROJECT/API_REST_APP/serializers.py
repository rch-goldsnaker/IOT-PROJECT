from rest_framework import  serializers

from .models import sensores

class SensoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = sensores
        fields = ['Tag','Ubicacion','Medicion','Valor','Fecha']
       