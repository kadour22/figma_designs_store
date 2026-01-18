from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import *
from .models import *

class project_service(APIView):
    
    def get(self, request,project_id=None):
        if project_id is not None:
            project = get_object_or_404(Project,id=project_id)
            serializer = display_project_serializer(project,many=False)
            return Response(serializer.data, status=200)
        else :
            projects = Project.objects.prefetch_related("images").all()
            serializer = display_project_serializer(projects,many=True)
            return Response(serializer.data, status=200)
    
    def post(self, request) :
        serializer = create_project_serializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, project_id) :
        project = get_object_or_404(Project,id=project_id)
        project.delete()
        return Response({"message" : f"{project.name} deleted"},status=status.HTTP_202_ACCEPTED)