from django.contrib import admin
from .models import *

admin.site.register(Menu)
admin.site.register(Panel)
admin.site.register(About)

#@admin.register(Menu)
#class MenuAdmin(admin.ModelAdmin):
  #  list_display = ['title', 'slug']


#@admin.register(Panel)
#class PanelAdmin(admin.ModelAdmin):
#    list_display = ['title', 'content', 'price']
