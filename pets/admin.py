from django.contrib import admin
from .models import Pet
from django.utils.html import format_html

class PetAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.pet_photo.url))

    thumbnail.short_description = 'Pet Image'
    list_display = ('id','thumbnail','pet_title', 'state', 'color', 'pet_type', 'pet_breed', 'age', 'gender', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'pet_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'pet_title', 'state', 'pet_type', 'pet_breed','age')
    list_filter = ('state', 'pet_type', 'age', 'gender')

admin.site.register(Pet, PetAdmin)
