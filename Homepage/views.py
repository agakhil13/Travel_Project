from django.shortcuts import render
from .models import Banner

# Create your views here.
def banner():
    ban1 = Banner()
    ban1.faded_text = "Enjoy the Best Destinations with Our Travel Agency"
    ban1.text = "Explore"
    ban1.bold_text = "The World"
    ban1.img = "slider-4-slide-1-1920x678.jpg"

    ban2 = Banner()
    ban2.faded_text = "A team of professional Travel Experts"
    ban2.text = "Trust"
    ban2.bold_text = "Our Experience"
    ban2.img = "slider-4-slide-2-1920x678.jpg"

    ban3 = Banner()
    ban3.faded_text = "Build your Next Holiday Trip with Us"
    ban3.text = "Create"
    ban3.bold_text = "Your Tour"
    ban3.img = "slider-4-slide-3-1920x678.jpg"

    ban = [ban1, ban2, ban3]
    return ban

def page(request):
    return render(request,'index.html', {'banner': banner()})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact-us.html')

def typography(request):
    return render(request,'typography.html')
