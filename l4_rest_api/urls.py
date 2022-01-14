"""REST API level app URL config"""

from rest_framework.routers import DefaultRouter

from .views import MovieViewSet, DirectorViewSet

app_name = "api"

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'directors', DirectorViewSet, basename='director')

urlpatterns = router.urls
