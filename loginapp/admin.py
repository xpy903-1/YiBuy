from django.contrib import admin

# Register your models here.
from loginapp.models import EntertainmentModel, CitysModel, NavigationModel


class EntertainmentModelAdmin(admin.ModelAdmin):
    list_display = ('picture', 'description', 'time')


class CitysModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_popular', 'start_str')
    fields = ('name', 'is_popular', 'start_str')


class NavigationModelAdmin(admin.ModelAdmin):
    list_display = ('img', 'img_name', 'img_id')


admin.site.register(EntertainmentModel, EntertainmentModelAdmin)
admin.site.register(CitysModel, CitysModelAdmin)
admin.site.register(NavigationModel, NavigationModelAdmin)
