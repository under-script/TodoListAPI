from rest_framework import routers
from todo_api.views import TodoViewSet

router = routers.SimpleRouter()
router.register(r'', TodoViewSet, basename='cities')
urlpatterns = router.urls