from rest_framework import serializers
from authe.models import Ticket_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket_model
        fields = ['ticket_id', 'subject', 'body',
                  'priority', 'email', 'phone', 'created_at']
