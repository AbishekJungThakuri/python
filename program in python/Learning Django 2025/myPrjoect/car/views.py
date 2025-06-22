from django.shortcuts import render,get_object_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets


# Create your views here.


class CarViewset(APIView):
    def get(self, request,id=None):
        if id:
            item = models.Cars.objects.get(id=id)
            serializer = serializers.CarSerializer(item)
            return Response({"status":"success", "data":serializer.data}, status=status.HTTP_200_OK)
        
        items = models.Cars.objects.all()
        serializer = serializers.CarSerializer(items, many=True)
        return Response({"status":"success", "data":serializer.data}, status=status.HTTP_200_OK)
    

    def post(self, request):
        serializer = serializers.CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        

    def patch(self, request, id=None):
        if not id:
          return Response(
            {"status": "error", "data": "ID is required for updating a record."},
            status=status.HTTP_400_BAD_REQUEST
          )
    
        try:
           item = models.Cars.objects.get(id=id)
        except models.Cars.DoesNotExist:
           return Response(
            {"status": "error", "data": f"Car with ID {id} does not exist."},
            status=status.HTTP_404_NOT_FOUND
           )
    
        serializer = serializers.CarSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
          serializer.save()
          return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
          return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

     
    def delete(self, request, id=None):
        item = models.Cars.objects.get(id=id)
        print(item)
        item.delete()
        return Response({"status":"success","data":"Item Deleted"})
        
