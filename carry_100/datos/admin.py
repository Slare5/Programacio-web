from django.contrib import admin
from .models import Tipo, Subcategoria, Lenguaje

# Register your models here.
admin.site.register( Tipo )
admin.site.register( Subcategoria )
admin.site.register( Lenguaje )