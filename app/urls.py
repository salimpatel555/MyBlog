from os import name
from django.urls import path
from app. views import profile,blog,signup, login,logout,blog_post,blog_detail,detele,edit


urlpatterns = [
    path('',blog,name='blog'),
    path('signup/',signup,name='signup'),
    path('profile/',profile,name='profile'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('blog_post/',blog_post,name='blog_post'),
    path('blog_detail/<str:id>',blog_detail,name='blog_detail'),
    path('edit/<str:id>',edit,name='edit'),
    path('delete/<int:id>',detele,name='detele'),
   


]