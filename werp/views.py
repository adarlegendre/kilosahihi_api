from django.shortcuts import render
from django.contrib.auth.models import User, Group
from werp.models import Farms,FarmProduce,Farmers,FarmReturnOfficers,Transactions 
from rest_framework import viewsets
from rest_framework import permissions
from werp.serializers import UserSerializer, GroupSerializer, FarmersSerializer,FarmProduceSerializer,FarmsSerializer, TransactionsSerializer, FarmReturnOfficersSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class FarmsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Farms.objects.all()
    serializer_class = FarmsSerializer
    permission_classes = [permissions.IsAuthenticated]

class FarmProduceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = FarmProduce.objects.all()
    serializer_class =FarmProduceSerializer
    permission_classes = [permissions.IsAuthenticated]

class FarmReturnOfficersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = FarmReturnOfficers.objects.all()
    serializer_class = FarmReturnOfficersSerializer
    permission_classes = [permissions.IsAuthenticated]

class TransactionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    permission_classes = [permissions.IsAuthenticated]

class FarmersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Farmers.objects.all()
    serializer_class = FarmersSerializer
    permission_classes = [permissions.IsAuthenticated]
