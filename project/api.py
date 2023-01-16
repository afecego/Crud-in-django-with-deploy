from .models import Project
from rest_framework import viewsets, permissions
from .serializer import ProjectSerializers

class ProjectViewsets(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class = ProjectSerializers