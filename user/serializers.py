from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import User

class RegisterSerializer(DocumentSerializer):
    class Meta:
        model = User
        fields = '__all__'
