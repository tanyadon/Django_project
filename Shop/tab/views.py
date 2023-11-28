from django.shortcuts import render
from tab.models import Sale
import random
# Create your views here.
def my_page(requiest):
    return render(requiest, 'index.html', {'object_list': Sale.objects.all() })