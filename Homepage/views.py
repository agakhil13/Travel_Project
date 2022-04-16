from ssl import HAS_TLSv1_3
from django.shortcuts import render
from .models import Banner, Box_Category, Hot_Tour, Teams, Wonder

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

def hot_tour():
    ht1 = Hot_Tour()
    ht1.title = "Shimla, Himachal Pradesh"
    ht1.img = "hottour1.jpg"
    ht1.desc = "The town is famous for pleasant walking experiences on hillsides surrounded by pine and oak forests. This capital city of Himachal Pradesh is famous for The Mall, ridge, and toy train. With colonial style buildings, the town has relics of ancient past that lend it a distinct look."
    ht1.review = 44
    ht1.price = 250
    ht1.rating = range(0,3)

    ht2 = Hot_Tour()
    ht2.title = "Coimbatore, Tamil Nadu"
    ht2.img = "hottour2.jpg"
    ht2.desc = "Coimbatore is also famous for foundry and automobile industries, manufacturing of textile industry equipment's, spares, motor pump sets, wet grinders and varied engineering goods and services. The development of Hydro electricity from the Pykara Falls in the 1930 led to a cotton boom in Coimbatore."
    ht2.review = 23
    ht2.price = 200
    ht2.rating = range(0, 4)

    ht3 = Hot_Tour()
    ht3.title = "Gangtok, Sikkim"
    ht3.img = "hottour3.jpg"
    ht3.desc = "Gangtok is also known as the land of monasteries due to the sheer number of monasteries it houses. It has emerged as a major Buddhist pilgrimage center and has some of the finest monasteries in India that you cannot afford to miss. The Rumtek monastery is undoubtedly one of the greatest monasteries in the country."
    ht3.review = 67
    ht3.price = 350
    ht3.rating = range (0, 2)

    ht = [ht1, ht2, ht3]
    return ht
def teams():
    t1 = Teams()
    t1.name = "Rakesh Yadav"
    t1.status = "Owner, Founder"
    t1.phone = "+91 7788996644"
    t1.img = "owner.jpg"

    t2 = Teams()
    t2.name = "Rohini Sharma"
    t2.status = "Travel Agent"
    t2.phone = "+91 9933446677"
    t2.img = "travelagent.jpg"

    t3 = Teams()
    t3.name = "Amit Singh"
    t3.status = "Tour Consultant"
    t3.phone = "+91 8880997766"
    t3.img = "tourconsultant.jpg"

    team = [t1, t2, t3]
    return team
def wonder():
    w1 = Wonder()
    w1.img = "wondertour1.jpg"
    w2 = Wonder()
    w2.img = "wondertour2.jpg"
    w3 = Wonder()
    w3.img = "wondertour3.jpg"
    w4 = Wonder()
    w4.img = "wondertour4.jpg"
    w5 = Wonder()
    w5.img = "wondertour5.jpg"
    w6 = Wonder()
    w6.img = "wondertour6.jpg"
    w7 = Wonder()
    w7.img = "wondertour7.jpg"
    
    wonders = [w1, w2, w3, w4, w5, w6, w7]
    return wonders

def page(request):
    return render(request,'index.html', {'banner': banner(), 'boxes': box_category(), 'hottours': hot_tour(), 'teams': teams(), 'wondertours':wonder()})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact-us.html')

def typography(request):
    return render(request,'typography.html')
