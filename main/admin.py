import datetime
from django.contrib import admin
from .models import Worker,Service,Visiting
# Register your models here.
@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name','surname','work_experience')
    list_filter = ('name','surname','work_experience')
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    list_filter = ('name','price')
    
    def show_visitors(self, obj):
        return "\n".join([a.visitor_name for a in obj.visitor_set.all()])
    
    
class VisitingAdmin(admin.ModelAdmin):
    list_display = ['worker', 'customer_name', 'date', 'time']
    list_filter = ('worker','date','time')
    actions = ['generate_records']

    def generate_records(self, request, queryset):
        for obj in queryset:
            if obj.time is not None:
                start_time = datetime.datetime.combine(obj.date, obj.time)
            else:
                start_time = datetime.datetime.combine(obj.date, datetime.time(0, 0))
                
            for time_str in ['09:00', '10:40', '12:40', '14:20', '16:00', '17:40', '18:20', '19:50']:
                time = datetime.datetime.strptime(time_str, '%H:%M').time()
                record_time = datetime.datetime.combine(obj.date, time)
                if record_time >= start_time:
                    Visiting.objects.create(
                        worker=obj.worker,
                        date=obj.date,
                        time=time,
                    )
        self.message_user(request, "Записи успешно созданы.")

    generate_records.short_description = "Создать записи"

admin.site.register(Visiting, VisitingAdmin)