from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category


# Create your views here.

@api_view()
def categories(request):
    return Response(
        {
            "ok": True,
            "categories": Category.objects.all(),
        }
    )
