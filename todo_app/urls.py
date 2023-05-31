from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register('tasks', views.TaskViewSet)
router.register('tags', views.TagViewSet)

urlpatterns = router.urls
