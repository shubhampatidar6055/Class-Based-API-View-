from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class Studentapi(APIView):
    def post(self,request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res = {"message":"Data created sucessfully"}
            return Response(res)
        return Response({"message":serializer.errors})
    
    def get(self,request):
        stu = Student.objects.all()
        serialzer = StudentSerializer(stu, many = True)
        return Response(serialzer.data)
    
    def get(self,request):
        data = request.data
        id = data.get('id')
        stu = Student.objects.filter(id=id)
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def put(self,request):
        data = request.data
        id = data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {"message":"Data updated sucessfully"}
            return Response(res,status=status.HTTP_201_CREATED)
        return Response({"message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request):
        data = request.data
        id = data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {"message":"Student deleted sucessfully"}
        return Response(res) 
