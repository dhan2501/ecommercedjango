from django.shortcuts import render, redirect
# encoding password... libary import
from django.contrib.auth.hashers import check_password
from stores.models.customer import Customer
from django.views import View


class Login(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer = Customer.get_customer_by_email(email)
        # print(customer)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                return redirect('homepage')
            else:
                error_message = 'Email or password invalid!!'
        else:
            error_message = 'Email or password invalid!!'
        print(email, password)
        return render(request, 'login.html', {'error' : error_message})
    
