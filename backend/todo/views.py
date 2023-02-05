from rest_framework import viewsets
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import HttpRequest
from .serializers import ProductSerializer, EmailSerializer
from .models import Product, Email
import easyocr
import smtplib
import time
import re


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        cover = request.data['nameFile']
        title = request.data['title']
        Product.objects.create(title=title, cover=cover)
        

def upload_path(instance, filname):
    return '/'.join(['covers', str(instance.title), filname])

def extract_date():
    reader = easyocr.Reader(['en'],gpu=False)
    res = reader.readtext("/covers/Latte/scad3.jpeg",detail=0)
    return res[3]


#def send_email(request):
    deadline = extract_date()
    message = "PROVA"+deadline
    email = smtplib.SMTP("smtp.gmail.com",587)
    email.ehlo()
    email.starttls()
    email.login("alessandro.miragliotta.am@gmail.com","sajahqdznlxbyzea")
    email.sendmail("alessandro.miragliotta.am@gmail.com","alessandro.miragliotta.am@gmail.com",message)
    email.quit()
    return HttpResponse("Mail Sent!")
  


class EmailView(APIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

    def post(self, request, format=None):
            address = request.data['email']
            cover = request.data['nameFile']
            title = request.data['title']
            time.sleep(1)
            reader = easyocr.Reader(['en'],gpu=False)
            time.sleep(1) 
            res = reader.readtext("/backend/modia/covers/"+title+"/"+cover.name,detail=0)
            #res = reader.readtext("/home/alessandro/django-react-app/backend/modia/covers/Latte/scad3.jpeg",detail=0)
            time.sleep(5)
            for i in range(len(res)):
                date = re.search('^[0-3]?[0-9].[0-3]?[0-9].(?:[0-9]{2})?[0-9]{2}$',res[i])
                if date:
                    break
            deadline = date.group(0)
            #deadline = extract_date()
            time.sleep(1) 
            message = deadline
            time.sleep(1) 
            
            email = smtplib.SMTP("smtp.gmail.com",587)
            email.ehlo()
            email.starttls()
            email.login("","")
            email.sendmail("",address,"Deadline "+message)
            email.quit()
    

    

    


    
    


    






