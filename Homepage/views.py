from django.shortcuts import render
from .models import Banner, Box_Category

# Create your views here.
def banner():
    ban1 = Banner()
    ban1.faded_text = "Enjoy the Best Destinations with Our Travel Agency"
    ban1.text = "Explore"
    ban1.bold_text = "The World"
    ban1.img = "ban1.jpg"

    ban2 = Banner()
    ban2.faded_text = "A team of professional Travel Experts"
    ban2.text = "Trust"
    ban2.bold_text = "Our Experience"
    ban2.img = "ban2.jpg"

    ban3 = Banner()
    ban3.faded_text = "Build your Next Holiday Trip with Us"
    ban3.text = "Create"
    ban3.bold_text = "Your Tour"
    ban3.img = "ban3.jpg"

    ban = [ban1, ban2, ban3]
    return ban

def box_category():
    box1 = Box_Category()
    box1.title = "Snow Holidays"
    box1.img = "box1.jpg"

    box2 = Box_Category()
    box2.title = "Mountain Holidays"
    box2.img = "box2.jpg"

    box3 = Box_Category()
    box3.title = "Beach Holidays"
    box3.img = "box3.jpg"

    box = [box1, box2, box3]
    return box

def page(request):
    return render(request,'index.html', {'banner': banner(), 'boxes': box_category()})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact-us.html')

def typography(request):
    return render(request,'typography.html')
