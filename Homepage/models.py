from django.db import models

# Create your models here.

class Banner:
    id : int
    faded_text : str
    text : str
    bold_text : str
    img : str

