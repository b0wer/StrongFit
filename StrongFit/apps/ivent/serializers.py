from rest_framework import serializers
from .models import ivent

class create_ivent(serializers.ModelSerializer):
    class Meta:
        model = ivent
        fields = '__all__'
        
class get_ivent(serializers.ModelSerializer):
    class Meta:
        model = ivent
        fields = '__all__'
    
class refresh_ivent(serializers.ModelSerializer):
    class Meta:
        model = ivent
        image = serializers.ImageField(
            max_length = None, use_url=True
        )
        fields = '__all__'