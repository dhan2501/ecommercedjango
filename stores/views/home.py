from django.shortcuts import render
from stores.models.products import Product
from stores.models.category import Category
# Create your views here.

def index(request):
    # products = Product.get_all_products()
    products =None
    categories = Category.get_all_categories()
    # print(request.GET['category'])
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()
    data = {}
    data['products'] = products
    data['categories'] = categories
    # print(products)
    return render(request, 'index.html', data)