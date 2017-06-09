from django.shortcuts import *
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .models import DataTable, FileModel
from .serializers import DataSerializer


# Create your views here.

class ListDatas(APIView):
    parser_classes = (FormParser,MultiPartParser)

    def get(self, request):
        datatables = DataTable.objects.all()
        serializer = DataSerializer(datatables, many=True)
        return Response(serializer.data)

    def post(self, request):
        files = request.data.pop('files')
        data_serial = DataSerializer(data=request.data)
        if data_serial.is_valid():
            datatable = data_serial.save()
            for file in files:
                FileModel.objects.create(datatable=datatable, file=file)
            return Response(data_serial.data, status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)



def upload(request):
    return render(request, "upload.html", {})
