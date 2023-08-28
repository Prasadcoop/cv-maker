# from django.shortcuts import render
# from .models import Note_api
# from rest_framework import viewsets
# from .serializers import NoteSerializer
# # Create your views here.
   

# class NoteListView(viewsets.ModelViewSet):
#     queryset = Note_api.objects.all()
#     serializer_class = NoteSerializer

from rest_framework import viewsets
from .models import Note_api
from .serializers import NoteSerializer


# Create your views here.

class NoteListView(viewsets.ModelViewSet):
    queryset = Note_api.objects.all()
    serializer_class  = NoteSerializer
