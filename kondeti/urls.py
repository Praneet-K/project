from django.urls import path

from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('addPost/',views.addPost,name='addPost'),
    path('display/<username>',views.display,name='display'),
]