from django.db import models
from django.contrib.auth.models import User

class Society(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Societies"

class Flat(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE, related_name='flats')
    flat_number = models.CharField(max_length=50)
    floor = models.IntegerField()
    is_occupied = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.society.name} - Flat {self.flat_number}"

class ResidentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    flat = models.ForeignKey(Flat, on_delete=models.SET_NULL, null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    is_owner = models.BooleanField(default=False)
    move_in_date = models.DateField()
    
    def __str__(self):
        return f"{self.user.username} - {self.flat if self.flat else 'No Flat Assigned'}"
