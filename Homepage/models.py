from django.db import models

# Create your models here.

class Banner:
    id : int
    faded_text : str
    text : str
    bold_text : str
    img : str

class Box_Category:
    id: int
    title : str
    img : str

class Hot_Tour:
    id : int
    title : str
    desc : str
    review : int
    img : str
    price : int
    rating: list


