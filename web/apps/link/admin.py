from django.contrib import admin

# Register your models here.
from link.models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

admin.site.register(Link, LinkAdmin)