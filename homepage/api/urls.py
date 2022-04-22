from django.urls import path
from homepage.api.views import *

urlpatterns = [
    path('authors', AuthorListCreateAPIView.as_view(), name='author-list'),
    path('categories', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('publishers', PublisherListCreateAPIView.as_view(), name='publisher-list'),
    path('contents', ContentListCreateAPIView.as_view(), name='content-list'),
]