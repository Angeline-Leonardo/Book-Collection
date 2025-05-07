from rest_framework import viewsets
from .models import LearningItem
from .serializers import LearningItemSerializer

class LearningItemViewSet(viewsets.ModelViewSet):
    queryset = LearningItem.objects.all().order_by('-added_on')
    serializer_class = LearningItemSerializer
