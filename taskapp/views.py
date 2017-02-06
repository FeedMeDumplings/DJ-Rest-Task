from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView

from django.contrib.auth import get_user_model

from .serializers import TaskSerializer, UserSerializer

from .models import Task

class TaskViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)	# only Authenticaed Users can perforom CRUD operations
	# queryset = Task.objects.all().order_by('-date_created')
	# queryset = Task.objects.all() 	# We use Filters for Ordering so remove order_by
	model = Task
	serializer_class = TaskSerializer
	filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
	filter_fields = ('task_completed',)
	ordering = ('-date_created',)
	# '^' Starts-with search
	# '=' Exact matches
	# '@' Full-text search (only for django's MySQL backend)
	# '$' Regex search
	search_fields = ('=task_name',)

	def get_queryset(self):
		"""
		return Task belonging to current user
		"""
		queryset = self.model.objects.all().filter(user=self.request.user)
		return queryset

	def perform_create(self, serializer):
		"""
		Associate current user as Task Owner
		"""
		return serializer.save(user=self.request.user)


# The two endpoints below are combined into one using filter

# class DueTaskViewSet(viewsets.ModelViewSet):
# 	queryset = Task.objects.all().order_by('-date_created').filter(task_completed=False)
# 	serializer_class = TaskSerializer

# class CompletedTaskViewSet(viewsets.ModelViewSet):
# 	queryset = Task.objects.all().order_by('-date_created').filter(task_completed=True)
# 	serializer_class = TaskSerializer


class CreateUserView(CreateAPIView):
	##########  CreateAPIView provide only POST method #######
	model = get_user_model()
	
	#  set Permission as AllowAny User to Register
	permission_classes = (AllowAny,)
	serializer_class = UserSerializer