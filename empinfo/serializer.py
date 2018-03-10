from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from empinfo.models import *
from django.contrib.auth.models import User


class CreateEmployeeRecord_serializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Employee
        fields = ("id", "first_name", "last_name", "grades", "owner", "email")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # employeedetails = serializers.HyperlinkedRelatedField(many=True, view_name='employee-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email')

    def get_username(self, obj):
        return str(obj.username)


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(view_name='employee-highlight', format='html')

    class Meta:
        model = Employee
        fields = ('url', 'id', 'first_name', 'last_name', 'owner', 'email')
