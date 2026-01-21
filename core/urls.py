from django.urls import path
from .views import project_service, project_image_service

urlpatterns = [
    path("projects/", project_service.as_view()),
    path("projects/<int:project_id>/", project_service.as_view()),

    path("images/", project_image_service.as_view()),
]