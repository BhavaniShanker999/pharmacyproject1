import django_filters 
from .models import *

class customer_order_filter(django_filters.FilterSet):
    class Meta:
        model=Order
        fields='__all__'
        exclude=['customer','date_created']

class customer_filter(django_filters.FilterSet):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['date_created']