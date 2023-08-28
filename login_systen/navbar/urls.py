from django.urls import path,include

from navbar import views

urlpatterns = [
   
   path('',views.homepage,name='homepage'),
   path('second/',views.secondpage,name='secondpage'),
   path('resumebuilder/',views.resume,name='resume'),
   path('addResume/',views.addresume,name='addResume'),
   path('viewResume/', views.viewResume, name='viewResume'),
   path('webscrap/',views.scrape_data,name='webscrap'),
   path('listofResume/',views.listResume,name='listResume'),
   path('<int:id>/', views.viewResume, name="viewResume"),
   path('generate_resume/', views.resumepdf, name='generate_resume'),
   path('logout/', views.logout, name='logout'),
]