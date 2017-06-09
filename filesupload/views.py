from django.shortcuts import *
from rest_framework.views import APIView
from .models import DataTable, FileModel
from .serializers import DataSerializer
from rest_framework.response import Response
from django.views.generic.edit import FormView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.status import HTTP_201_CREATED


from django.forms import modelformset_factory
# Create your views here.

class ListDatas(APIView):
    parser_classes = (FormParser,MultiPartParser)

    def get(self, request):
        datatables = DataTable.objects.all()
        serializer = DataSerializer(datatables, many=True)
        return Response(serializer.data)

    def post(self, request):
        print request.data
        data_serial = DataSerializer(data=request.data)
        if data_serial.is_valid():
            data_serial.save()
            return Response(data_serial.data, status=HTTP_201_CREATED)



def upload(request):
    return render(request, "upload.html", {})
