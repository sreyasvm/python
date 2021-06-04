from django.shortcuts import render
from .models import Library

# Create your views here.


def insert_library_details(schema):
    print("In insert libaray details")
    text = "Library " + schema
    lib = Library(name = text, rating=5)
    lib.save()
    return lib
