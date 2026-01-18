from rest_framework import serializers
from .models import *


class create_project_serializer(serializers.ModelSerializer) :
    class Meta :
        model = Project
        fields = ["name","descriptions","price","prototype_url"]


class project_images_serializer(serializers.ModelSerializer):
    class Meta :
        model = ProjectImage
        fields = "__all__"

class display_project_serializer(serializers.ModelSerializer) :
    images = project_images_serializer(many=True, read_only=True)
    class Meta :
        model = Project
        fields = ["name","descriptions","price","prototype_url","images"]

class project_images_serializer(serializers.ModelSerializer):
    class Meta :
        model = ProjectImage
        fields = "__all__"