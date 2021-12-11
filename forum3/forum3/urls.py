from django.contrib import admin
from django.urls import path
from app1.views import *
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('addInForum/',addInForum,name='addInForum'),
    path('addInDiscussion/',addInDiscussion,name='addInDiscussion'),
]