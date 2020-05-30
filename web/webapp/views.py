from django.shortcuts import render
import json


# Create your views here.
from . import data_retrieve
from .constants import INDEX_TEMPLATE_PATH


def index(request):
    data = data_retrieve.get_data()
    print(data)
    return render(request, INDEX_TEMPLATE_PATH, {'DataFrame':data})