from rest_framework import viewsets
from .models import Entry
from .serializers import EntrySerializer

class EntryViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Entry.objects.all().order_by('-id')
	serializer_class = EntrySerializer
	paginate_by = 2