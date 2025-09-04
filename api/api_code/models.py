from django.db import models

# Create your models here.
class flight(models.Model):
    airline = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=10)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.airline} flight {self.flight_number}"