from django.db import models


class DeliveryDepartment(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Courier(models.Model):
    full_name = models.CharField(max_length=200)
    department = models.ForeignKey(DeliveryDepartment, related_name='couriers', on_delete=models.SET_NULL, null=True) #on_delete=models.SET_NULL  предотвращает удаление курьеров при удалении отдела.
    undelivered_orders_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.full_name


class DeliveryMethod(models.Model):
    TRANSPORT_CHOICES = [
        ('bike', 'Велосипед'),
        ('car', 'Автомобиль'),
        ('scooter', 'Скутер'),
    ]
    courier = models.OneToOneField(Courier, related_name='delivery_method', on_delete=models.CASCADE)
    transport = models.CharField(max_length=50, choices=TRANSPORT_CHOICES)

    def __str__(self):
        return f"{self.get_transport_display()} - {self.courier.full_name}"


class Order(models.Model):
    courier = models.ForeignKey(Courier, related_name='orders', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=200)
    order_date = models.DateTimeField()
    estimated_delivery_date = models.DateTimeField()

    def __str__(self):
        return f"Order #{self.id} - {self.status}"
