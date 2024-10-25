from django.contrib import admin
from api2.models import Barber


# Register your models here.
class BarberAdmin(admin.ModelAdmin):
    list_display = ['id','name','money','t1','t2','t3','t4','t5','t6','t7','t8','t9','t10','t11','t12','t13','t14','t15','t16','t17','t18','t19','t20','t21','t22','t23','t24']

admin.site.register(Barber, BarberAdmin)