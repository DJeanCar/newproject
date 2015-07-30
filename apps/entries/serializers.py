from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Entry, Comment

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'username')

class EntrySerializer(serializers.ModelSerializer):

	user = UserSerializer()
	comments = serializers.SerializerMethodField()

	def get_comments(self, entry):
		return Comment.objects.filter(entry = entry).count()

	class Meta:
		model = Entry
		fields = ('id','comments' ,'user','title', 'content', 'image')


class CommentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Comment
		fields = ('id', 'comment')