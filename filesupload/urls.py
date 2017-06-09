from django.conf.urls import url
from . import views
from views import ListDatas, upload
urlpatterns = [
        url(r'^$', ListDatas.as_view(), name='upload'),
        url(r'^upload/$', upload)
        ]