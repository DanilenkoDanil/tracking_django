from django.contrib import admin
from .models import Signal, SignalResult, Marathon, Setting


@admin.register(Signal)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'price', 'source', 'date',)


@admin.register(SignalResult)
class DealAdmin(admin.ModelAdmin):
    list_display = ('id', 'signal', 'name', 'type', 'price', 'price_change', 'source', 'date',)


@admin.register(Marathon)
class DealAdmin(admin.ModelAdmin):
    list_display = ('id', 'channel', 'current_balance', 'start_balance', 'leverage')


@admin.register(Setting)
class DealAdmin(admin.ModelAdmin):
    list_display = ('id', 'channel_for_bot',)
