from django.conf.urls import include, url

from rest_framework_nested import routers
from .viewsets import EntryViewSet, CommentViewSet
from .views import IndexView, IndexView2

router = routers.SimpleRouter()
router.register(r'entradas', EntryViewSet)
# router.register(r'comentarios', CommentViewSet)
comment_router = routers.NestedSimpleRouter(router, r'entradas', lookup='entry')
comment_router.register(r'comentarios', CommentViewSet)

urlpatterns = [
	
	url(r'^$', IndexView.as_view()),
	url(r'^prueba2/$', IndexView2.as_view()),
	url(r'^ajax/$', 'apps.entries.views.my_ajax'),
	url(r'^guardar-entrada/$', 'apps.entries.views.save_entry'),

    url(r'^api/', include(router.urls)),
    url(r'^api/', include(comment_router.urls)),
]
