from django.shortcuts import render
from django.shortcuts import redirect
# encoding password... libary import
from django.contrib.auth.hashers import make_password
# from stores.models.products import Product
from stores.models.customer import Customer
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
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
        
        error_message = self.validateCustomer(customer)
    
        if not error_message:
            # print(first_name, last_name, email, password, phone)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = { 
                    'error' : error_message,
                    'values' : value
                    }
        # return HttpResponse(request.POST.get('email'))
            return render(request, "signup.html", data)
        
    def validateCustomer(self, customer):
            error_message = None
            if not customer.first_name:
                error_message = "First name required!!"
            elif len(customer.first_name) < 4:
                error_message = "First name must be 4 char long or more"
            elif not customer.last_name:
                error_message = "Last Name Required!!"
            elif len(customer.last_name) < 4:
                error_message = "Last name must be 4 char or more"
            elif not customer.phone:
                error_message = "Phone number required!!"
            elif len(customer.phone) < 10:
                error_message ="Enter phone number valid according valid digit"
            elif not customer.email:
                error_message = "Email required!!"
            elif len(customer.email)<6:
                error_message = "Email must be 5 char long"
            elif not customer.password:
                error_message = "Password must be required!!"
            elif len(customer.password) < 6:
                error_message = "Password must be 6 char"

            # Email verification code.....
            elif customer.isExists():
                error_message = "Given email address already registers...."

            return error_message