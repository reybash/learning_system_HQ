from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Lesson
from .serializers import LessonSerializer


# Create your views here.


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Lesson.objects.filter(product__accesses__user=user,
                                     product__accesses__is_valid=True)
