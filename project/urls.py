from rest_framework import routers
from .api import ProjectViewsets

router = routers.DefaultRouter()

router.register('api/project', ProjectViewsets, 'projects')

urlpatterns = router.urls