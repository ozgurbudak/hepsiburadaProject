from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from hepsiburadaSociality.Parser import Parser
from product.models import Product
from product.serializers import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        # create parser instance
        url = request.data['url']
        if url is None:
            return Response("url field is empty", status=status.HTTP_400_BAD_REQUEST)
        else:
            parser = Parser(url)
            parser_result = parser.parse()
            serializer = self.get_serializer(data=parser_result)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response("success", status=status.HTTP_200_OK)
