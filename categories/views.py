from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySerializer


# Create your views here.
class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
