from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import ProductService
from .serializers import ProductSerializer

class ProductView(APIView):
    def get(self, request, product_id=None):
        if product_id:
            product = ProductService.retrieve_product(product_id)
            if product:
                serializer = ProductSerializer(product)
                return Response(serializer.data)
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        products = ProductService.list_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = ProductService.create_new_product(serializer.validated_data)
            return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, product_id):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = ProductService.modify_product(product_id, serializer.validated_data)
            if product:
                return Response(ProductSerializer(product).data)
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        success = ProductService.remove_product(product_id)
        if success:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
