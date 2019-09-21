from django.urls import include, path
from rest_framework import routers
from .views import FilmView

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

router = routers.DefaultRouter()

urlpatterns = [
    path('', FilmView.as_view()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]