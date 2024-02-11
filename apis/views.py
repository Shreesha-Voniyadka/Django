# from django.shortcuts import render
# from todos import models
# from .serializers import TodoSerilizer
# # from rest_framework import generics
# from rest_framework import viewsets

# # Create your views here.
# # class ListTodo(generics.ListCreateAPIView):
# #     queryset = models.Todo.objects.all()
# #     serializer_class = TodoSerilizer
# # class DetailTodo(generics.RetrieveDestroyAPIView):
# #     queryset = models.Todo.objects.all()
# #     serializer_class = TodoSerilizer
# class TodoViewSet(viewsets.ModelViewSet):
#     queryset = models.Todo.objects.all()

from rest_framework.views import APIView
from rest_framework.response import Response

class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})