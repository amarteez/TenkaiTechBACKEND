# store/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import Category, Product, CartItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer

# View to handle category list
class CategoryListView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        categories_list = [{'id': category.id, 'name': category.name} for category in categories]
        return JsonResponse(categories_list, safe=False)

# View to handle product list by category
class ProductListView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        products_by_category = {}

        for category in categories:
            products = Product.objects.filter(category=category)
            products_by_category[category.id] = {
                'category_name': category.name,
                'products': [
                    {
                        'id': product.id,
                        'name': product.name,
                        'description': product.description,
                        'price': product.price,
                        'image': product.image,
                        'image_url': product.image_url
                    } for product in products
                ]
            }

        return JsonResponse(products_by_category, safe=False)

# View to handle cart items
class CartItemsView(View):
    def get(self, request, *args, **kwargs):
        cart_items = CartItem.objects.all()
        cart_items_data = [
            {
                'id': item.id,
                'product_id': item.product.id,
                'name': item.product.name,
                'price': item.product.price,
                'quantity': item.quantity
            }
            for item in cart_items
        ]
        return JsonResponse(cart_items_data, safe=False)

# View to add items to cart
@method_decorator(csrf_exempt, name='dispatch')
class AddToCartView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            product_id = data.get('product_id')
            quantity = data.get('quantity', 1)

            if not product_id:
                return JsonResponse({'error': 'Product ID is required'}, status=400)

            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return JsonResponse({'error': 'Product not found'}, status=404)

            # Find or create the cart item
            cart_item, created = CartItem.objects.get_or_create(product=product, defaults={'quantity': quantity})
            if not created:
                cart_item.quantity += quantity
                cart_item.save()

            return JsonResponse({
                'id': cart_item.id,
                'product_id': cart_item.product.id,
                'quantity': cart_item.quantity
            }, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

# View to remove items from cart
@method_decorator(csrf_exempt, name='dispatch')
class RemoveFromCartView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            cart_item_id = data.get('cart_item_id')

            if not cart_item_id:
                return JsonResponse({'error': 'Cart item ID is required'}, status=400)

            try:
                cart_item = CartItem.objects.get(id=cart_item_id)
                cart_item.delete()
                return JsonResponse({'message': 'Item removed from cart'}, status=200)
            except CartItem.DoesNotExist:
                return JsonResponse({'error': 'Cart item not found'}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

# View to render the product list HTML template
def index(request):
    return render(request, 'store/product_list.html')

# API view to get product list in JSON format
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# API view to get product detail in JSON format
@api_view(['GET'])
def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=404)
    
    serializer = ProductSerializer(product)
    return Response(serializer.data)
