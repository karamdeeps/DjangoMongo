from rest_framework.routers import DefaultRouter
from user.views import UserViewSet


router = DefaultRouter(trailing_slash=True)
router.register('company', UserViewSet)

urlpatterns = router.urls
