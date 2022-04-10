from django.contrib import admin
from .models import User,Category,Book
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id","first_name","last_name","is_active","staff","admin","created_at"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","label"]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id","name","book_image","category","created_at"]