import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from .serializers import (RegistrationSerializer, CustomAuthTokenSerializer, 
                        CustomTokenObtainSerializer, PasswordResetAPISerializer, 
                        ProfileAPISerializer, ResendActivationEmailSerializer,
                        PasswordResetRequestSerializer, PasswordResetSerializer
                    )
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.mail import send_mail
from accounts.models import Profile, PaswordReset
from mail_templated import EmailMessage
from ..utils import EmailThread

User = get_user_model()

class RegistrationApiView(GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            serializer.save()
            data = {
                'email': email,
            }
            user_obj = get_object_or_404(User, email=email)
            token = self.get_tokens_for_user(user_obj)

            email_obj = EmailMessage('email/registration.tpl', {'Token': token}, 'admin@gmail.com', to=[email])
            EmailThread(email_obj).run()
            return Response(data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
        })

class CustomDiscartAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer

class PasswordRestAPIViewTest(GenericAPIView):
    authentication_classes = [IsAuthenticated]
    serializer_class = PasswordResetAPISerializer
    model = User

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def put(self, request):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'details': 'Wrong Password'}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': [],
            }

            return Response(response)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
class ProfileAPIView(RetrieveUpdateAPIView):
    serializer_class = ProfileAPISerializer
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj

class TestAPIEmailSend(APIView):

    def get(self, request, *args, **kwargs):
        self.email = "admin@gmail.com"
        user_obj = get_object_or_404(User, email=self.email)
        token = self.get_tokens_for_user(user_obj)

        email_obj = EmailMessage('email/hello.tpl', {'Token': token}, 'admin@gmail.com', to=[self.email])
        EmailThread(email_obj).run()
        return Response("this is a test email")
    
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

class ActivateUserAPIView(APIView):

    def get(self, request, token, *args, **kwargs):
        try:
            Token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = Token.get('user_id')
        except ExpiredSignatureError:
            return Response({'details': 'the provided token is expired'})
        except InvalidSignatureError:
            return Response({'details': 'the provided token is invalid'})
        user_obj = User.objects.get(pk=user_id)
        if user_obj.is_verified:
            return Response({'details': 'the user is already verified'})
        
        user_obj.is_verified = True
        user_obj.save()
        return Response({'details': 'the user is successfully verified'})

class ResendActivateUserAPIView(GenericAPIView):
    serializer_class = ResendActivationEmailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.validated_data['user']
        token = self.get_tokens_for_user(user_obj)
        email_obj = EmailMessage('email/registration.tpl', {'Token': token}, 'admin@gmail.com', to=[user_obj.email])
        EmailThread(email_obj).run()
        return Response({'details': 'we resend the activation link'}, status=status.HTTP_200_OK)
    
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
    
class PaswordResetRequestView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = PasswordResetRequestSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.data.get('email')
        user = User.objects.filter(email__iexact=email).first()

        if user:
            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user)
            reset = PaswordReset(email=email, token=token)
            reset.save()

            reset_url_token = f"{token}"

            email_obj = EmailMessage('email/reset_password.tpl', {'reset_url_token': reset_url_token}, 'admin@gmail.com', to=[email])
            EmailThread(email_obj).run()

            return Response({'details': 'we send a email for you to reset your password!', 'user token': token}, status=status.HTTP_200_OK)
        else: 
            return Response({'details': 'User with this creadantials not found', 'email': email, 'user': user}, status=status.HTTP_404_NOT_FOUND)
        
class PasswordResetAPIView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = PasswordResetSerializer

    def post(self, request, token, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data

        reset_obj = PaswordReset.objects.filter(token=token).first()

        if not reset_obj:
            return Response({'details': 'Invalid Token!!'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.filter(email=reset_obj.email).first()

        if user:
            user.set_password(request.data['new_password'])
            user.save()

            return Response({'success': 'Password Rest confirmed'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'password reset failed'}, status=status.HTTP_400_BAD_REQUEST)
        

