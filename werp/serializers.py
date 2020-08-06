
from django.contrib.auth.models import  User, Group
from rest_framework import serializers
from werp.models import Farms,Farmers,FarmProduce,Transactions,FarmReturnOfficers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class FarmReturnOfficersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmReturnOfficers
        fields = ['name', 'address','phone','id_no','account_no','region','zone','gender','status']

class FarmersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Farmers
        fields = ['name', 'address','phone','id_no','account_no','region','zone','gender','status']

class FarmsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Farms
        fields = ['name', 'region','zone']

class FarmProduceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmProduce
        fields = ['name', 'desc','status']

class TransactionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transactions
        fields = ['farmer', 'fro','farm','date','weight','produce','status']




