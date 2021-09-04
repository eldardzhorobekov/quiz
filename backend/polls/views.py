from datetime import datetime

from .models import Poll
from rest_framework import generics

from .serializers import PollSerializer


class PollList(generics.ListAPIView):
    querializer_class = Poll
    serializer_class = PollSerializer

    def get_queryset(self):
        return Poll.objects.filter(date_end__gte = datetime.now()).order_by('date_start')
