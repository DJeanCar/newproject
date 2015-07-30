from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Entry, Comment
from .serializers import EntrySerializer, CommentSerializer

class EntryViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Entry.objects.all().order_by('-id')
	serializer_class = EntrySerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	# paginate_by = 2

	# def get_queryset(self):
	# 	return self.queryset.filter(user = self.request.user)

class CommentViewSet(viewsets.ViewSet):

	queryset = Comment.objects.all()

	def list(self, request, entry_pk):
		comments = self.queryset.filter(entry__pk = entry_pk)
		serializer = CommentSerializer(comments, many = True)
		return Response(serializer.data)

	def retrieve(self, request, pk, entry_pk):
		comment = get_object_or_404(Comment, pk = pk, entry__pk = entry_pk)
		serializer = CommentSerializer(comment)
		return Response(serializer.data)