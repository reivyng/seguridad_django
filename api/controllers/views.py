from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import User, Producto
from api.serializers.user_serializer import UserSerializer
from api.serializers.producto_serializer import ProductoSerializer

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductoListView(APIView):
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
