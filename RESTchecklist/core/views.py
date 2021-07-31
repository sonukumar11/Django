# from django.http.response import HttpResponse
from copy import error
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import CheckList, CheckListItem
from .serializers import CheckListSerializer , CheckListItemSerializer
from rest_framework import status
from django.http import Http404
from core import serializers
# Create your views here.

# @api_view()
# def test_api(request):
#     return Response({'Name':'Sonu Kumar Das'})

# class TestAPIView(APIView):
#     def get(self, request, format=None):
#        return Response({'Name':'Sonu Kumar Das From Class View'}) 


class CheckListAPIView(APIView):
    serializer_class = CheckListSerializer
    def get(self,request,format=None):
        data = CheckList.objects.all()
        serializer = self.serializer_class(data , many = True)
        serialized_data = serializer.data
        return Response(serialized_data , status = status.HTTP_200_OK)
    
    def post(self, request ,format=None):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data,status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#To get single checklist ... we are using primary key.
class CheckListsAPIView(APIView):
    serializer_class = CheckListSerializer

    def get_object(self,pk):
        try:
            return CheckList.objects.get(pk = pk)
        except CheckList.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        serializer = self.serializer_class(self.get_object(pk))
        Serialized_data = serializer.data
        return Response(Serialized_data,status=status.HTTP_200_OK)

    def put(self,request,pk,format=None):
        checklist = self.get_object(pk)
        serializer = self.serializer_class(checklist,data = request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format = None):
        checklist = self.get_object(pk)
        checklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CheckListItemCreateAPIView(APIView):
    serializer_class = CheckListItemSerializer
    def post(self, request ,format=None):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data,status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        
class CheckListItemAPIView(APIView):
    serializer_class = CheckListItemSerializer

    def get_object(self,pk):
        try:
            return CheckListItem.objects.get(pk = pk)
        except CheckListItem.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        checklist_item = self.get_object(pk)
        serializer = self.serializer_class(checklist_item)
        Serialized_data = serializer.data
        return Response(Serialized_data,status=status.HTTP_200_OK)

    def put(self,request,pk,format=None):
        checklist_item = self.get_object(pk)
        serializer = self.serializer_class(checklist_item ,data = request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format = None):
        checklist_item = self.get_object(pk)
        checklist_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def author(request):
    return HttpResponse("This REST API is created by Sonu Kumar Das")