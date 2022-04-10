from django.contrib import admin
from django.urls import path,include
from .views import Home_page,AddBook,UpdateBook,DeleteBook,Login_page,Signup_page

urlpatterns = [
                path("",Login_page.as_view(),name="login_page"),
                path("signup",Signup_page.as_view()),
                path("home",Home_page.as_view(),name="home_page"),
                path("addbook",AddBook.as_view()),
                path("updatebook/<int:pk>",UpdateBook.as_view()),
                path("deletebook/<int:pk>",DeleteBook.as_view())
]