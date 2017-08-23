
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.InventoryList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.InventoryDetail.as_view()),
]
