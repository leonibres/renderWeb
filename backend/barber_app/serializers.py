from rest_framework import serializers
from .models import Usuario, Appointment

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'email', 'username', 'nombre', 'apellido', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'username': {'required': False}  # Será generado automáticamente si no se proporciona
        }

    def create(self, validated_data):
        # Asegurarse de que username sea el email si no se proporciona
        if 'username' not in validated_data:
            validated_data['username'] = validated_data['email']

        try:
            # Usar create_user en lugar de create para hashear la contraseña
            user = Usuario.objects.create_user(
                email=validated_data['email'],
                username=validated_data['username'],
                password=validated_data['password'],
                nombre=validated_data.get('nombre', ''),
                apellido=validated_data.get('apellido', '')
            )
            return user
        except Exception as e:
            print("Error creando usuario:", str(e))
            raise serializers.ValidationError(str(e))

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ('user',)
