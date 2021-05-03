from django.shortcuts import get_object_or_404, render
from rest_framework.viewsets import ModelViewSet
from .models import Menu
from .serializers import MenuSerializer

# Create your views here.
class MenuViewSet(ModelViewSet):

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


def menu_detail(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    return render(request, "menu/detail.html", {"menu": menu})
