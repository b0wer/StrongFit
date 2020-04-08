from rest_framework import serializers
from .models import Post

    
class refresh_Post(serializers.ModelSerializer):
    class Meta:
        model = Post
        image = serializers.ImageField(
            max_length = None, use_url=True
        )
        fields = '__all__'

class create_Post(serializers.ModelSerializer):
    class Meta:
        model = Post
        image_pub = serializers.ImageField(
            max_length = None, use_url=True
        )
        fields = '__all__'
