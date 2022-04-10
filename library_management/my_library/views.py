from django.shortcuts import render,redirect
from django.views import View
from .models import Book,Category,User
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate,login as auth_login
from django.contrib import messages
# Create your views here.

class Login_page(View):
    def get(self,request):
        return render(request,"login.html")
    def post(self,request):
        user = authenticate(username=request.POST.get("email"), password=request.POST.get('password'))
        if user is not None:
            auth_login(request, user)
            context = {
                "user": request.user
            }

            return redirect("home_page")
        else:
            messages.error(request, '*Login details are not valid')
            return redirect("login_page")

class Signup_page(View):
    """
    This View Is Created For User Signup
    """
    def get(self,request):

        return render(request,"signup.html")

    def post(self,request):
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User(
            email = email,
            first_name= first_name,
            last_name= last_name,
            password= make_password(password))
        user.save()
        return redirect("login_page")


class Home_page(View):
    """
    This View Is Created For Home Page Showing All Books
    """
    def get(self,request):
        super_admin =  request.user.admin
        book = Book.objects.all()
        return render(request,"index.html",{"book_data":book,"super_admin":super_admin})

class AddBook(View):
    """
    This View Is Created For Add New Book On DataBase
    """
    def get(self,request):
        category = Category.objects.all()
        author  = Author.objects.all()
        return render(request,"book_add.html",{"category_data":category,"author_data":author})
    
    def post(self,request):
        book_name = request.POST.get("book_name")
        author_name = request.POST.get("author_name")
        book_category = request.POST.get("category")
        book_image = request.FILES['profilepic']
        
        book = Book(
                name = book_name,
                author_name=author_name,
                book_image=book_image,
                category=Category.objects.get(id=book_category))
        book.save()
        return redirect("home_page")


class UpdateBook(FormView):
    """
    This FormView Is Created For Update The Book
    """
    template_name = "book_update.html"

    def get_context_data(self, **kwargs):

        super_admin =  self.request.user.admin
        
        villa_context = {
            "book_data": Book.objects.get(pk=self.kwargs["pk"]),
            "category_data":Category.objects.all(),
            "super_admin":super_admin
        }
        return villa_context

    def post(self, request, *args, **kwargs):
        obj = Book.objects.get(pk=self.kwargs['pk'])
        data = request._get_post().dict()
        obj.name = request.POST.get("name")
        obj.author_name = request.POST.get("author_name")
        obj.book_image = request.FILES.get("book_image")
        obj.category = Category.objects.get(id=data["category"])
        obj.save()
        return redirect("home_page")

class DeleteBook(FormView):
    """
    This FormView Is Created For Delete The Book
    """
    def post(self, request, *args, **kwargs):
        obj = Book.objects.filter(pk=self.kwargs['pk'])
        data = request._get_post().dict()
        del data['csrfmiddlewaretoken']
        obj.delete()
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))