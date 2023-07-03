from django.contrib import admin
from django.urls import path
# from home.views import my_view
from home import views
from django.db import models  
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('' , views.blank , name = 'blank'),
    # path("about" , views.about , name = 'about'),
    # path("contact" , views.contact , name = 'contact'),
    # path("services" , views.services , name = 'services'),

    # path("start" , views.start , name = 'start'),
    # path("index" , views.index , name = 'index' )
    # path("about" , views.about , name = 'about') , 
    # path("services" , views.services , name = 'services'),
    # path("contact" , views.contacts , name = 'contacts')

 #  --------------------------------------------------------------------
          # Session 
    # path('ssession',views.setsession , name = 'setsession'),
    # path('gsession',views.getsession , name = 'getsession')

 #  ---------------------------------------------------------------------

       #Cookie set up

       path('scookie' , views.setcookie ,name = 'setcookie'),
       path('gcookie' , views.getcookie ,name = 'getcookie')

]

# if settings.DEBUG:
#     urlpatterns +=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) 

