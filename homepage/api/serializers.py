from homepage.models import *
from rest_framework import serializers

class ContentCreateSerializer(models.ModelSerializer):
    
    class Meta:
        model = Content
        fields = "__all__"
        
class ContentRetrieveSerializer(models.ModelSerializer):
    
    class Meta:
        model = Content
        fields = "__all__"
        
class AuthorCreateSerializer(models.ModelSerializer):
    
    class Meta:
        model = Author
        fields = "__all__"
        
class AuthorRetrieveSerializer(models.ModelSerializer):
    
    class Meta:
        model = Author
        fields = "__all__"
        
class CategoryCreateSerializer(models.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
        
class CategoryRetrieveSerializer(models.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
        
class PublisherCreateSerializer(models.ModelSerializer):

    class Meta:
        model = Publisher
        fields = "__all__"
        
class PublisherRetrieveSerialzier(models.ModelSerializer):
    
    class Meta:
        model = Publisher
        fields = "__all__"
        
class ContentSeriesCreateSerializer(models.ModelSerializer):
    
    class Meta:
        model = ContentSeries
        fields = "__all__"

class ContentSeriesRetrieveSerializer(models.ModelSerializer):
    
    class Meta:
        model = ContentSeries
        fields = "__all__"