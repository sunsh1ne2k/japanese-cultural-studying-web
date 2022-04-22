from homepage.models import *
from rest_framework import serializers

class ContentCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Content
        fields = "__all__"
        
class ContentRetrieveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Content
        fields = "__all__"
        
class AuthorCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = "__all__"
        
class AuthorRetrieveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = "__all__"
        
class CategoryCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
        
class CategoryRetrieveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
        
class PublisherCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = "__all__"
        
class PublisherRetrieveSerialzier(serializers.ModelSerializer):
    
    class Meta:
        model = Publisher
        fields = "__all__"
        
class ContentSeriesCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ContentSeries
        fields = "__all__"

class ContentSeriesRetrieveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ContentSeries
        fields = "__all__"