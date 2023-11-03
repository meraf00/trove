from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Product
from .serializers import ProductSerializer


def get_object(pk):
    try:
        return Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return None


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def products_create_list(request):
    """
    Create or list all products.
    """

    if request.method == "GET":
        return get_products(request)

    elif request.method == "POST":
        if request.user.is_authenticated:
            return create_product(request)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([AllowAny])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def product_detail_update_delete(request, pk):
    """
    Retrieve, update or delete a product instance.
    """

    if request.method == "GET":
        return get_product(request, pk)

    elif request.method == "PUT":
        if request.user.is_authenticated:
            return update_product(request, pk)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    elif request.method == "DELETE":
        if request.user.is_authenticated:
            return delete_product(request, pk)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


def get_products(request):
    """
    List all products.
    """

    paginator = PageNumberPagination()
    paginator.page_size = request.GET.get("page_size", 10)

    products = Product.objects.all()
    result_page = paginator.paginate_queryset(products, request)
    serializer = ProductSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


def get_product(request, pk):
    """
    Retrieve a product instance.
    """

    product = get_object(pk)

    if product:
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    return Response(status=status.HTTP_404_NOT_FOUND)


def create_product(request):
    """
    Create a new product.
    """

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def update_product(request, pk):
    """
    Update a product instance.
    """

    product = get_object(pk)

    if not product:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_product(request, pk):
    """
    Delete a product instance.
    """

    product = get_object(pk)

    if not product:
        return Response(status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
