from django.urls import path
from homepage.api.views import *

urlpatterns = [
    path('authors', 
         AuthorListCreateAPIView.as_view(), 
         name='author-list'),
    
    path('authors/<int:pk>', 
         AuthorListCreateAPIView.as_view(), 
         name='author-detail'),
    path('categories', CategoryListCreateAPIView.as_view(), name='category-list'),
    
    path('categories/<int:pk>', 
         CategoryDetailAPIView.as_view(),
         name='category-detail'),

    path('publishers', 
         PublisherListCreateAPIView.as_view(), 
         name='publisher-list'),
    
    path('publishers/<int:pk>', PublisherDetailAPIView.as_view(),
         name='publisher-detail'),

    path('contents', 
         ContentListCreateAPIView.as_view(), 
         name='content-list'),
    
    path('contents/<int:pk>', 
         ContentDetailAPIView.as_view(), 
         name='content-detail'),

]
