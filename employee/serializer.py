from rest_framework import serializers
from.models import employee


class employeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = employee
        #fileds = ('firstname', 'lastname')
        fields = '__all__'