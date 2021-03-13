from rest_framework.views import APIView
from rest_framework.response import Response
from . models import User
from . serializers import RegisterSerializer
from rest_framework import status

class Register(APIView):
       def post(self,request):
        user_data = RegisterSerializer(data = request.data)
        if user_data.is_valid():
            user_data.save()
            return Response(user_data.data,status = status.HTTP_201_CREATED)
        return Response(user_data.errors,status = status.HTTP_400_BAD_REQUEST)