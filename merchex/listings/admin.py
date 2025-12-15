from django.contrib import admin
from listings.models import Band,Listings


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')
    
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'sold', 'band')    

admin.site.register(Band, BandAdmin)
admin.site.register(Listings, ListingAdmin)

