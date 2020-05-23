from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_extensions.mixins import NestedViewSetMixin

from api.models import Comment, Post
from api.serializers import CommentSerializer, PostSerializer


class CommentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """Comments API"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """Posts API"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpvoteView(APIView):
    """View for incrementing upvotes for post"""

    def get(self, request, post_id):
        """GET action handler"""

        post = Post.objects.filter(pk=post_id).first()

        if not post:
            return Response(
                {"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND,
            )

        post.upvote()

        return Response({"message": "You successfully upvoted the post!"})
