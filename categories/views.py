from rest_framework.exceptions import NotFound
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
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()
            return Response(
                CategorySerializer(new_category).data,
            )
        else:
            return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
def category(reqeust, pk):
    try:
        category = Category.objects.get(pk=pk)
    except:
        raise NotFound

    if reqeust.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif reqeust.method == "PUT":
        serializer = CategorySerializer(
            category,
            data=reqeust.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_category = serializer.save()
            return Response(CategorySerializer(updated_category).data)
        else:
            return Response(serializer.errors)
    