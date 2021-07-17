from django.contrib import admin
from django.urls import path
from bank_app.views import about,add_customer,login,view_customer,transfer_money,logout,transfer_history

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",login,name="login"),
     path('logout/',logout,name = 'logout'),	
    path("about/",about,name="about"),
    path("add_customer/",add_customer,name="add_customer"),
    path("view_customer/",view_customer,name="view_customer"),
    path("transfer_money/",transfer_money,name="transfer_money"),
    path("transfer_history/",transfer_history,name="transfer_history"),
    	

]
