# store/admin.py
#from django.contrib import admin
#from .models import Category, Product

#class ProductInline(admin.TabularInline):
#    model = Product
#    extra = 1  # Número de formularios vacíos para añadir nuevos productos

#class CategoryAdmin(admin.ModelAdmin):
#    list_display = ('name',)
#    inlines = [ProductInline]

#class ProductAdmin(admin.ModelAdmin):
#    list_display = ('name', 'price', 'category')
#    list_filter = ('category',)
#    search_fields = ('name',)

#admin.site.register(Category, CategoryAdmin)
#admin.site.register(Product, ProductAdmin)
