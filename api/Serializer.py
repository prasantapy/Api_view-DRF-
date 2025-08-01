from rest_framework.serializers import ModelSerializer
from api.models import Job_Profile
class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Job_Profile
        fields = '__all__'