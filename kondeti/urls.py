from django.urls import path

from . import views
urlpatterns=[
    path('',views.home,name='kondeti-home'),
    path('addPost/',views.addPost,name='kondeti-addPost'),
    path('display/<userid>/',views.display,name='kondeti-display'),
    path('displaypost/<int:pk>/',views.displaypost,name='kondeti-displaypost')
]