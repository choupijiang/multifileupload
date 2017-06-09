# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.db import models

# Create your models here.

class DataTable(models.Model):
    name = models.CharField(max_length=200, verbose_name="数据表名")


class FileModel(models.Model):
    file = models.FileField(upload_to="images", verbose_name="文件名")
    datatable = models.ForeignKey(DataTable, related_name="files")
