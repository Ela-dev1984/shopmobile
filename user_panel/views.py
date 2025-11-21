from django.shortcuts import HttpResponse
from admin_panel.models  import Mobile

def all(request):
     allmobile = Mobile.objects.all()
     content = "<br>".join([f"{b.id}-{b.mobile_name}"for b in allmobile])
     return HttpResponse(f"<center><h1>liste mobileha:{content}</center></h1>")
 
 
 
def sort(request,bishine,kamine):
    list = Mobile.objects.filter(price__range=(bishine,kamine)).order_by("price")
    content = "<br>".join([f"{b.id}-{b.mobile_name}"for b in list])
    return HttpResponse(f"<center><h1>liste morede nazare shoma:{content}</center></h1>")


def search(request,search):
    list = Mobile.objects.filter(mobile_name__icontains=search)
    content = "<br>".join([f"{b.id}-{b.mobile_name}"for b in list])
    return HttpResponse(f"<center><h1>liste mobilehaye{search}:{content}</center></h1>")
     
