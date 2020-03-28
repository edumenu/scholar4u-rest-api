from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
# Specify a basename if the ViewSet doesn't have a query set or you want to override the name of the query set
# associated with it
router.register('posts', views.PostsViewSet)
router.register('comments', views.CommentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]