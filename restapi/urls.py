"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings


# from taskapp.views import TaskViewSet
from taskapp import views

router = routers.DefaultRouter()
# Trying simple router (but we can also use default router)
# router = routers.SimpleRouter()


router.register(r'task', views.TaskViewSet, 'get_queryset')

# Since we combined the API endpoints for task_due and task_completed
# into one and put it under one TaskViewSet, the two router.register
# are not required

# router.register(r'due_task', views.DueTaskViewSet)
# router.register(r'completed_task', views.CompletedTaskViewSet)


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^register/$', views.CreateUserView.as_view(), name='user'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# for media
# you can also use
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


