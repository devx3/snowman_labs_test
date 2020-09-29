from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (
    RegistrationViewSet,
    LoginViewSet
)

AccountsRouter = SimpleRouter()
AccountsRouter.register('register', RegistrationViewSet, basename='register')
AccountsRouter.register('login', LoginViewSet, basename='login')
