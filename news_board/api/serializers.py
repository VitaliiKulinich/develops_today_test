from rest_framework import serializers

from api.models import Comment, Post


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    """API serializer of comments"""

    class Meta:
        model = Comment
        fields = ["id", "post", "author_name", "content", "creation_date"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    """API serializer of posts"""

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "link",
            "creation_date",
            "amount_of_upvotes",
            "author_name",
        ]
