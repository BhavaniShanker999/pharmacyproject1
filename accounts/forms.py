from .models import *
from django.forms import ModelForm

#Registration and Login related imports
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# finished the imports related to registration and login


class create_user_form(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class create_order(ModelForm):
    class Meta:
        model= Order
        fields= '__all__'
        exclude=['customer']

class create_customer_form(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'

class create_product_form(ModelForm):
    class Meta:
        model=Product
        fields='__all__'
        exclude=['category']