from django.contrib import admin

from .models import Profile
from offers.models import Offer


class OfferInline(admin.TabularInline):
    model = Offer


class OfferAdmin(admin.ModelAdmin):
    inlines = [OfferInline]


admin.site.register(Profile, OfferAdmin)
