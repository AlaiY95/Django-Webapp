from django.contrib import admin
from supplychain.models import Country, Pollutant, PollutantEntry

# Register your models here.
admin.site.register(Country)
admin.site.register(Pollutant)
admin.site.register(PollutantEntry)