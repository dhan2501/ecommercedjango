from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

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

        # Validation
        value = {
            'first_name' : first_name,
            'last_name' : last_name,
            'phone' : phone,
            'email' : email
        }
        error_message = None

        customer = Customer(first_name = first_name,
                                last_name = last_name,
                                email = email,
                                password = password,
                                phone = phone)

        if not first_name:
            error_message = "First name required!!"
        elif len(first_name) < 4:
            error_message = "First name must be 4 char long or more"
        elif not last_name:
            error_message = "Last Name Required!!"
        elif len(last_name) < 4:
            error_message = "Last name must be 4 char or more"
        elif not phone:
            error_message = "Phone number required!!"
        elif len(phone) < 10:
            error_message ="Enter phone number valid according valid digit"
        elif not email:
            error_message = "Email required!!"
        elif len(email)<6:
            error_message = "Email must be 5 char long"
        elif not password:
            error_message = "Password must be required!!"
        elif len(password) < 6:
            error_message = "Password must be 6 char"

        # Email verification code.....
        elif customer.isExists():
            error_message = "Given email address already registers...."

        #saving data

        if not error_message:
            print(first_name, last_name, email, password, phone)
            customer.register()
            return redirect('homepage')
        else:
            data = { 
                    'error' : error_message,
                    'values' : value
                    }
        # return HttpResponse(request.POST.get('email'))
            return render(request, "signup.html", data)