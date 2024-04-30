from rest_framework import serializers

from Api.models import Department, LegalInstrument, Service


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'

    def create(self, valdated_data):
        instance = Service.objects.create(**valdated_data)
        return instance


class LegalInstrumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = LegalInstrument
        fields = "__all__"

    def create(self, valdated_data):
        instance = LegalInstrument.objects.create(**valdated_data)
        return instance


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"

    def create(self, valdated_data):
        instance = Department.objects.create(**valdated_data)
        return instance
