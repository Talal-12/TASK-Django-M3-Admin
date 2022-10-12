from django.contrib import admin
from .models import Pokemon

# Register your models here.
# admin.site.register(Pokemon, PokemonAdmin)


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "hp", "active",)
    list_display_links = ("id", "name",)
    list_filter = ("active",)

    fieldsets = (
        (
            "general", {
                'fields': ('name', 'hp', 'active', 'type',)
            }
        ),
        (
            "Localizations", {
                "fields": ("name_fr", "name_ar", "name_jp",),
                "classes": ('collapse',)
            }
        ),
        (
            None, {
                'fields': ('created_at', 'updated_at',)
            }
        )
    )


admin.site.register(Pokemon, PokemonAdmin)
