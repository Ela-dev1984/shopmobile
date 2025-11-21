from django.shortcuts import HttpResponse
from .models import Mobile,Admin

def home(request,username,password):
    Admin.objects.create(username=username,password=password)
    return HttpResponse(f"<center><h1>sabtenam movafaghiat amiz bood.</center></h1>")
    

def add_mobile(request,mobile_name,price,password):
   
  if not Admin.objects.filter(password=password).exists():
       
    return HttpResponse(f"<center><h1>ramze Admin dorost nist.</center></h1>")
  
  Mobile.objects.create(mobile_name=mobile_name,price=price,password=password)
  return HttpResponse(f"<center><h1> mobile ezafe shod.</center></h1>")

  
     
def info(request,password):
     
    if not Admin.objects.filter(password=password).exists():
      return HttpResponse(f"<center><h1>ramze Admin dorost nist.</center></h1>")
    
    pas = Mobile.objects.get(password=password)
    allmobile = Mobile.objects.all()
    count = allmobile.count()
    allprice = 0
    for item in allmobile:
      allprice += item.price
    return HttpResponse(f"<center><h1> tedade kole mobilha:{count}<br> ghemate kole mobileha{allprice}<br>")
                 
         
 


    
    

    


