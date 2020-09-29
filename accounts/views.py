from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import RegistrationSerializer
from django.contrib import auth
from rest_framework.authtoken.models import Token


class RegistrationViewSet(
        mixins.CreateModelMixin,
        viewsets.GenericViewSet):
    """
    Create a new user in API
    """
    permission_classes = [
        permissions.AllowAny,
    ]

    def create(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)

        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


class LoginViewSet(
        mixins.CreateModelMixin,
        viewsets.GenericViewSet):
    """
    Used to return the user's token
    """
    permission_classes = [
        permissions.AllowAny,
    ]

    def create(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)

            resp = {'token': token.key}
            return Response(resp, status=status.HTTP_200_OK)
        return Response({
            'msg': 'Username or Password are invalid.'
        }, status=status.HTTP_400_BAD_REQUEST)
