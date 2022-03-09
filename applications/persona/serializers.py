from rest_framework import serializers

from .models import Persona

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = ('id', 'nombre', 'apellido', 'tipo_documento', 
                'documento', 'hobbie' )