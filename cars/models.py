from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='cars_photos/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    phone_number = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'