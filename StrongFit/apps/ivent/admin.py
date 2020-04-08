from django.contrib import admin
from .models import ivent, IventUserProfile, IventUserProfile_photo 
# Register your models here.

admin.site.register(ivent)

class GalleryInline(admin.TabularInline):
    fk_name = 'IventUserProfile'
    model = IventUserProfile_photo

@admin.register(IventUserProfile)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]