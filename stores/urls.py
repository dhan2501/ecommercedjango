from django.contrib import admin
from django.urls import path
# from .views import index, signup, login #when use login as a function.
# from .views import index, Signup, Login # when using login as a class
# from .views import home, signup, login  #Method 1 code

# Using method 2
from .views.home import index
from .views.signup import Signup
from .views.login import Login


# Method 1:
# urlpatterns = [
#     path('', home.index, name="homepage"),
#     path('signup', signup.Signup.as_view()),
#     path('login', login.Login.as_view())
# ]

# Method 2:
urlpatterns = [
    path('', index, name="homepage"),
    path('signup', Signup.as_view()),
    path('login', Login.as_view())
]