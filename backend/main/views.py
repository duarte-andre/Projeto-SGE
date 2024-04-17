from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, BasePermission


class CustomDeadlinePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.has_perm('main.view_deadline')
        else:
            return request.user.has_perm(['main.add_deadline', 'main.delete_deadline', 'main.change_deadline'])



class DeadlineView(ModelViewSet):
    queryset = Deadline.objects.all()
    serializer_class = DeadlinesSerializer
    permission_classes = (CustomDeadlinePermission,)
