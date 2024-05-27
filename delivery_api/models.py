from django.db import models


class DeliveryDepartment(models.Model):
    external_id = models.CharField(primary_key=True, max_length=255)
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name


class Courier(models.Model):
    external_id = models.CharField(primary_key=True, max_length=255)
    department = models.ForeignKey(
        DeliveryDepartment,
        related_name='couriers',
        on_delete=models.CASCADE
    )
    undelivered_orders_count = models.PositiveIntegerField(default=0)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    start_date = models.BigIntegerField(null=True, blank=True)
    vehicle_type = models.IntegerField(max_length=50, null=True, blank=True)
    license_number = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.middle_name}"
