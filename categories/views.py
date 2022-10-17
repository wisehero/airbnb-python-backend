from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category
from .serializers import CategorySerializer


# Create your views here.

@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response({"categories": serializer.data})
    elif request.method == "POST":
        Category.objects.create(
            name=request.data["name"],
            kind=request.data["kind"],
        )
        return Response({"created": True})


@api_view()
def category(reqeust, pk):
    category = Category.objects.get(pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)
