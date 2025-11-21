
from django.urls import path
from .views import home,add_mobile,info


urlpatterns = [
  
    path("home/<str:username>/<str:password>/",home,name="home"),
    path("add_mobile/<str:mobile_name>/<int:price>/<str:password>/",add_mobile,name="add"),
    path("info/<str:password>/",info,name="info"),
]
