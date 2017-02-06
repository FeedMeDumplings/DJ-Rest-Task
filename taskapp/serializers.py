from rest_framework import serializers

from .models import Task
from django.contrib.auth import get_user_model


class TaskSerializer(serializers.ModelSerializer):
	user = serializers.CharField(source='user.username', read_only=True)	# We dont want input for this field, it is auto
	image = serializers.ImageField(max_length=None, use_url=True)
	doc = serializers.FileField(max_length=None, use_url=True)

	class Meta:
		model = Task
		fields = ('id', 'user', 'task_name', 'task_desc', 'date_created', 'task_completed', 'image', 'doc')


class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)

	#  we override Create mothod
	def create(self, validated_data):
		user = get_user_model().objects.create(
				username=validated_data['username']
		)						
		# assuming there is a custom auth model or built-in auth model
		# custom auth model can be set using AUTH_USER_MDOEL in settings.py
		user.set_password(validated_data['password'])	# we dont want to serialize password because it is hashed
		user.save()
		return user

	class Meta:
		model = get_user_model()
		fields = ('username', 'password')
