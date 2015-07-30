from django.conf.urls import include, url

from rest_framework import routers
from .viewsets import EntryViewSet

router = routers.SimpleRouter()
router.register(r'entradas', EntryViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
