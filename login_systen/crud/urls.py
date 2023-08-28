
from django.urls import path,include
from crud import views

urlpatterns = [

    path('index/',views.index,name='index'),
    path('showdata/',views.showdetails,name='showdetails'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>', views.update), 
    path('delete/<int:id>', views.Delete, name='Delete'), 
    
]