from rest_framework import serializers
from .models import DataTable, FileModel
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = ('file')


class DataSerializer(serializers.ModelSerializer):

    files = FileSerializer(required=True, many=True)

    class Meta:
        model = DataTable
        fields = ('id', 'name', 'files')

    def create(self, validated_data):
        print "**",validated_data
        files = validated_data.pop('files')
        print "++", files
        data_table = DataTable.objects.create(**validated_data)
        for file_data in files:
            print file_data
            print FileModel.objects.create(**file_data)
        return data_table