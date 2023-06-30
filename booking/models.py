from django.db import models


class Table(models.Model):
    number = models.IntegerField(verbose_name='table number')

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = 'Table'
        verbose_name_plural = 'Tables'


class Booking(models.Model):
    name = models.CharField(max_length=255, verbose_name='name and surname')
    phone_number = models.CharField(max_length=20, verbose_name='phone number')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name='table number')
    datetime = models.CharField(max_length=20, verbose_name='Booking date and time')

    def __str__(self):
        return f"Booking for {self.name} at {self.datetime} on the table {self.table}"

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
