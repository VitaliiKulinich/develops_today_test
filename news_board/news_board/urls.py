"""news_board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from api.views import CommentViewSet, PostUpvoteView, PostViewSet


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    """Mixin class for nested routing"""


urlpatterns = [
    path("api/posts/<int:post_id>/upvote/", PostUpvoteView.as_view()),
]

router = NestedDefaultRouter()

authors_router = router.register("api/posts", PostViewSet)
authors_router.register(
    "comments",
    CommentViewSet,
    basename="posts-comments",
    parents_query_lookups=["post"],
)

urlpatterns += [
    path("", include(router.urls)),
]
