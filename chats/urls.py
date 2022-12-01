from django.urls import path
from .views import*


urlpatterns =[
    path('delete/<int:pk>/post/', Deletepost.as_view(), name='details_delete'),
    path('edit/<int:pk>/post/', Editpost.as_view(), name='details_edit'), 
    path('new/post/', Createpost.as_view(), name='new_post'),
    path('details/<int:pk>/', Detailview.as_view(), name='details_view'),
    path('about', About.as_view(), name= 'About'),
    path("", Homepage.as_view(), name="home"),
    path("contacts", Contact.as_view(), name="contact"),
    path("private", Privacy.as_view(), name="privacy"),
]

