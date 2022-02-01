

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProductSerializer, ReviewSerializer, TagSerializer
from .models import Product, Review, Tag
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from main.models import Product
from main.serializer import ProductSerializer
from rest_framework.pagination import PageNumberPagination


class ProductCreateListAPIview(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination


class ProductDetailUpdateDeleteAPIview(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer()
    lookup_field = 'id'



class ReviewCreateListAPIview(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination


class ReviewDetailUpdateDeleteAPIview(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer()
    lookup_field = 'id'


class TagCreateListAPIview(ListCreateAPIView):
    queryset = Tag.objects.filter(is_active=True)
    serializer_class = TagSerializer
    pagination_class = PageNumberPagination


class TagDetailUpdateDeleteAPIview(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer()
    lookup_field = 'id'




# @api_view(['GET'])
# def get_product(request):
#     product = Product.objects.all()
#     data = ProductSerializer(product, many=True).data
#     return Response(data=data)


# @api_view(['GET'])
# def get_detail(request, id):
#     try:
#         product = Product.objects.get(id=id)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND,
#                         data={'error': 'Product not found!'})
#     data = ProductSerializer(product).data
#     return Response(data=data)


# @api_view(['GET'])
# def get_review(request):
#     review = Review.objects.all()
#     data = ReviewSerializer(review, many=True).data
#     return Response(data=data)


# @api_view(['GET'])
# def get_tags(request):
#     tag = Tag.objects.filter(is_active=True)
#     data = TagSerializer(tag, many=True).data
#     return Response(data=data)
