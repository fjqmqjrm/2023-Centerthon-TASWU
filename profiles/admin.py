# profiles/admin.py

from django.contrib import admin
from .models import UserProfile, Station

admin.site.register(UserProfile)
admin.site.register(Station)
