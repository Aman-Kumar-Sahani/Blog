from .models import Blog
from .serializers import BlogSerializer
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission
from rest_framework.views import APIView
from django.views import generic
from django.shortcuts import render 

class PostList(generic.ListView):
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.filter(status=1).order_by('-ddate_modified')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    permission_classes = [IsAuthenticated]
    model = Blog
    template_name = 'post_detail.html'

class BlogAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        blog_data= Blog.objects.all()
        serialize_org = BlogSerializer(blog_data,many=True)
        return Response(serialize_org.data)
    
    def post(self,request):
        blog_data = BlogSerializer(data = request.data)
        if blog_data.is_valid():
            blog_data.save()
            return Response(blog_data.data,status = status.HTTP_201_CREATED)
        return Response(Blog_data.errors,status = status.HTTP_400_BAD_REQUEST)

class BlogDetailsBy_ID(APIView):
    permission_classes = [IsAuthenticated]
   
    def get_object(self,id):
        try:
            return Blog.objects.get(id = id)
        except Blog.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        blog_data = self.get_object(id)
        serialize_data = BlogSerializer(blog_data) 
        return Response(serialize_data.data)
    
    def put(self,request,id):
        stu_data = self.get_object(id)
        serialize_data = BlogSerializer(stu_data, data = request.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data)
        return Response(serialize_data.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        blog_data = self.get_object(id)
        blog_data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

