from django.contrib import admin
from .models import Train, SeatAvabilty, Compartment
# Register your models here.


class TrainAdmin(admin.ModelAdmin):
    list_display = ('train_id', 'train_name', 'schedule_date')
    list_display_links = ["train_id", "train_name"]

admin.site.register(Train, TrainAdmin)


class CompartmentAdmin(admin.ModelAdmin):
    list_display = ('comp_id', 'name')

admin.site.register(Compartment, CompartmentAdmin)

class SeatAvabiltyAdmin(admin.ModelAdmin):
    list_display = ('seat_id', 'comp_id', 'train_id', 'seat_no','status')

admin.site.register(SeatAvabilty, SeatAvabiltyAdmin)