from django.contrib import admin
from pokemon.models import Pokemon

# Register your models here.

admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):     
    list_display = ('id', 'name', 'hp' ,'active')
    list_filter = ('active',)
    list_display_links = ('id', 'name')
    fieldsets = (
    (None, {
        'fields':('name', 'type', 'hp', 'active'),

    }),
        ('Localizations', {
        'classes': ('collapse',),
        'fields': ('name_fr' ,'name_ar','name_jp'),
    }),
    
    )
admin.site.register(Pokemon,PokemonAdmin)
