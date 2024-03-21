from django.shortcuts import render, redirect
from stores.models.products import Product
from stores.models.category import Category
from django.views import View
# Create your views here.

class Index(View):
    
    def post(self, request):
        product = request.POST.get('product')
        print(product)
        return redirect('homepage')


    def get(self, request):
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
        print('Your are:',request.session.get('email'))
        return render(request, 'index.html', data)



# def index(request):
#     # products = Product.get_all_products()
#     products =None
#     categories = Category.get_all_categories()
#     # print(request.GET['category'])
#     categoryID = request.GET.get('category')
#     if categoryID:
#         products = Product.get_all_products_by_categoryid(categoryID)
#     else:
#         products = Product.get_all_products()
#     data = {}
#     data['products'] = products
#     data['categories'] = categories
#     # print(products)
#     print('Your are:',request.session.get('email'))
#     return render(request, 'index.html', data)