from rest_framework import serializers

from .models import Note_api

class NoteSerializer(serializers.ModelSerializer):
   class Meta:
       model = Note_api
       fields = ('title', 'description', 'amount', 'quantity','iscompleted')

