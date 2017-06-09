from rest_framework import serializers

from .models import DataTable, FileModel


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = ('file','id')


class DataSerializer(serializers.ModelSerializer):

    files = FileSerializer(many=True)

    class Meta:
        model = DataTable
        fields = ('id', 'name', 'files')

    def create(self, validated_data):
        files = validated_data.pop('files')
        data_table = DataTable.objects.create(**validated_data)
        return data_table