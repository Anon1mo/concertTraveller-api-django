from django.contrib import admin

from .models import Offer, Chat


class ChatInline(admin.TabularInline):
    model = Chat


class ChatAdmin(admin.ModelAdmin):
    inlines = [ChatInline]


admin.site.register(Offer, ChatAdmin)