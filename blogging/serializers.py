from rest_framework.serializers import ModelSerializer

from .models import Post, Comment
from auth_manager.models import CustomUser


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username')


class PostSerializer(ModelSerializer):
    author = AuthorSerializer()
    
    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(ModelSerializer):
     
    class Meta:
        model = Comment
        fields = "__all__"
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['user'] = self.instance.user.username
        return ret

