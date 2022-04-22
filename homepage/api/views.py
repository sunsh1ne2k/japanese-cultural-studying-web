from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status

from homepage.models import *

from homepage.api.serializers import *


class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorCreateSerializer

    def list(self, request, format=None):
        queryset = Author.objects.all()
        serializer = AuthorRetrieveSerializer(queryset,
                                              many=True)
        return Response(serializer.data)

    def create(self, request, format=None):
            serializer = AuthorCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                latest_author = Author.objects.last()
                detail = AuthorRetrieveSerializer(latest_author)
                return Response(detail.data, status=status.HTTP_201_CREATED)
            return Response(detail.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer

    def list(self, request, format=None):
        queryset = Category.objects.all()
        serializer = CategoryRetrieveSerializer(queryset,
                                              many=True)
        return Response(serializer.data)

    def create(self, request, format=None):
            serializer = CategoryCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                latest_author = Category.objects.last()
                detail = CategoryRetrieveSerializer(latest_author)
                return Response(detail.data, status=status.HTTP_201_CREATED)
            return Response(detail.errors, status=status.HTTP_400_BAD_REQUEST)

class PublisherListCreateAPIView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherCreateSerializer

    def list(self, request, format=None):
        queryset = Publisher.objects.all()
        serializer = PublisherRetrieveSerialzier(queryset,
                                              many=True)
        return Response(serializer.data)

    def create(self, request, format=None):
            serializer = PublisherCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                latest_author = Publisher.objects.last()
                detail = PublisherRetrieveSerialzier(latest_author)
                return Response(detail.data, status=status.HTTP_201_CREATED)
            return Response(detail.errors, status=status.HTTP_400_BAD_REQUEST)


class ContentListCreateAPIView(generics.ListCreateAPIView):

    queryset = Content.objects.all()
    serializer_class = ContentCreateSerializer

    def list(self, request, format=None):
        queryset = Content.objects.all()
        serializer = ContentRetrieveSerializer(queryset,
                                               many=True)
        return Response(serializer.data)

    def create(self, request, format=None):
        serializer = ContentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            latest_content = Content.objects.last()
            detail = ContentRetrieveSerializer(latest_content)
            return Response(detail.data, status=status.HTTP_201_CREATED)
        return Response(detail.errors, status=status.HTTP_400_BAD_REQUEST)
