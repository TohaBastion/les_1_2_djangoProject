from django.http import HttpResponse


def shop_home(request):
    return HttpResponse('Shop Home')


def shop_product(request, product_id):
    return HttpResponse(f'Id of product: {product_id}')



