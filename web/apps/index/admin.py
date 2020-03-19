from django.contrib import admin
from index.models import Carousel


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('article', 'is_active')


admin.site.register(Carousel, CarouselAdmin)