from django.contrib import admin
from . models import Test
from . models import Author

# Register your models here.

admin.site.register(Test)
admin.site.register(Author)