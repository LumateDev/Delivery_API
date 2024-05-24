from django.contrib import admin
from .models import DeliveryDepartment, Courier


class DeliveryDepartmentAdmin(admin.ModelAdmin):
    list_display = ('external_id', 'department_name')  # Поля, которые будут отображаться в списке
    search_fields = ('external_id', 'department_name')  # Поля, по которым будет доступен поиск
    ordering = ('department_name',)  # Сортировка по умолчанию


admin.site.register(DeliveryDepartment, DeliveryDepartmentAdmin)


class CourierAdmin(admin.ModelAdmin):
    list_display = (
        'external_id', 'first_name', 'last_name', 'middle_name', 'email',
        'phone_number', 'start_date', 'vehicle_type', 'license_number',
        'undelivered_orders_count', 'department'
    )
    list_filter = ('vehicle_type', 'department')  # Фильтры сбоку
    search_fields = ('external_id', 'first_name', 'last_name', 'middle_name', 'email',
                     'phone_number')  # Поля, по которым будет доступен поиск
    ordering = ('last_name', 'first_name')  # Сортировка по умолчанию
    # Если вы хотите разрешить сортировку по ForeignKey, добавьте 'department__department_name'

    #raw_id_fields = ('department',)  # Для удобства выбора ForeignKey (если записей много)


admin.site.register(Courier, CourierAdmin)
