from django.shortcuts import render
from django.http import HttpResponse

from .models.products import Product
from .models.category import Category
from .models.customer import Customer
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

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        postData = request.POST
        first_name = postData.get('fname')
        last_name = postData.get('lname')
        email = postData.get('email')
        password= postData.get('password')
        phone = postData.get('phone')
        print(first_name, last_name, email, password, phone)
        customer = Customer(first_name = first_name,
                            last_name = last_name,
                            email = email,
                            password = password,
                            phone = phone)
        customer.register()
        # return HttpResponse(request.POST.get('email'))
        return HttpResponse("signup success")