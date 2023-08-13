# profiles/admin.py

from django.contrib import admin
from .models import UserProfile, Station, TaxiCall

admin.site.register(UserProfile)
admin.site.register(Station)
admin.site.register(TaxiCall)
