from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse
from .serializers import UsuarioSerializer, AppointmentSerializer
from .models import Usuario, Appointment
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request, format=None):
    return Response({
        'register': reverse('register', request=request, format=format),
        'login': reverse('login', request=request, format=format),
        'logout': reverse('logout', request=request, format=format),
        'appointments': reverse('appointment-list', request=request, format=format),
        'my-appointments': reverse('my-appointments', request=request, format=format),
    })

@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        print("Datos de registro recibidos:", request.data)
        data = request.data.copy()
        
        # Garantizar que username es igual a email si no se envió
        if not data.get('username') and data.get('email'):
            data['username'] = data.get('email')
        
        try:
            # Validar si ya existe el email
            if Usuario.objects.filter(email=data.get('email')).exists():
                return Response({
                    'email': ['Este correo electrónico ya está en uso.']
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Validar si ya existe el username
            if Usuario.objects.filter(username=data.get('username')).exists():
                return Response({
                    'username': ['Este nombre de usuario ya está en uso.']
                }, status=status.HTTP_400_BAD_REQUEST)
                
            serializer = UsuarioSerializer(data=data)
            if serializer.is_valid():
                user = serializer.save()
                return Response({
                    'message': 'Usuario registrado exitosamente',
                    'user': UsuarioSerializer(user).data
                }, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            print("Error en registro:", str(e))
            return Response({
                'detail': f'Error en el servidor: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # Agregar método OPTIONS para manejar preflight CORS
    def options(self, request, *args, **kwargs):
        response = Response()
        response["Allow"] = "POST, OPTIONS"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]
    
    def post(self, request):
        logger.info("Datos recibidos para login: %s", request.data)
        
        email_or_username = request.data.get('email') or request.data.get('username')
        password = request.data.get('password')
        
        if not email_or_username or not password:
            return Response({
                'error': 'Por favor proporcione email/usuario y contraseña'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Buscar usuario por email o username
            user = Usuario.objects.filter(email=email_or_username).first() or \
                   Usuario.objects.filter(username=email_or_username).first()
            
            if not user:
                return Response({
                    'error': 'Credenciales inválidas'
                }, status=status.HTTP_401_UNAUTHORIZED)
            
            # Autenticar usando el username real del usuario
            auth_user = authenticate(request, username=user.username, password=password)
            
            if auth_user:
                login(request, auth_user)
                # Asegura que la sesión esté guardada
                request.session.save()
                response = Response({
                    'message': 'Login exitoso',
                    'user': UsuarioSerializer(auth_user).data,
                    'sessionid': request.session.session_key
                })
                # CORS y cookies
                origin = request.headers.get('Origin', '*')
                response['Access-Control-Allow-Credentials'] = 'true'
                response['Access-Control-Allow-Origin'] = origin
                return response
            
            return Response({
                'error': 'Credenciales inválidas'
            }, status=status.HTTP_401_UNAUTHORIZED)
            
        except Exception as e:
            logger.error("Error en login: %s", str(e), exc_info=True)
            return Response({
                'error': 'Error en el servidor'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # Agregar método OPTIONS para manejar preflight requests correctamente
    def options(self, request, *args, **kwargs):
        response = Response()
        response["Allow"] = "POST, OPTIONS"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response

@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Sesión cerrada exitosamente'})

class AppointmentList(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Solo citas del usuario autenticado
        return Appointment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Asignar el usuario autenticado a la cita
        serializer.save(user=self.request.user)

class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Solo permitir acceso a las citas del usuario autenticado
        return Appointment.objects.filter(user=self.request.user)

class MyAppointments(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Appointment.objects.filter(user=self.request.user)
