from rest_framework.viewsets import ModelViewSet
from .models import Meal, Menu
from .serializers import MealSerializer, MenuSerializer

# Create your views here.


class MealViewSet(ModelViewSet):

    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class MenuViewSet(ModelViewSet):

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
