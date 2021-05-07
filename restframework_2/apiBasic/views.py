from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from . import models
from .serializer import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins

class ArticleViews(APIView):
    def get(self, request):
        article = models.Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
class ArticleDetail(APIView):
    def get_object(self, pk):
        try:   
            articles = models.Article.objects.get(pk = pk)
        except models.Article.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk):
        articles = self.get_object(pk)
        serializer = ArticleSerializer(articles)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        articles = self.get_object(pk)
        articles.delete()
        return Response(status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        articles = self.get_object(pk)
        serializer = ArticleSerializer(articles, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)   

            
    
        
