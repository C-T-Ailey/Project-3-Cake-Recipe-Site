from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

FLAVOURS = (
    ('0', 'Plain Sponge'),
    ('1', 'Caramel'),
    ('2', 'Chocolate'),
    ('3', 'Cream Cheese'),
    ('4', 'Fruit'),
    ('5', 'Spiced'),
    ('6', 'Vanilla')
)
# Create your models here.

class Cake(models.Model):
    name = models.CharField(max_length=100)
    flavours = models.CharField(max_length=20, choices=FLAVOURS, default=FLAVOURS[0][0])
    description = models.TextField(max_length=250)
    imageurl = models.CharField(default=None, blank=True, max_length=300, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'pk': self.id})

    def __str__(self):
        return f"{self.name}"

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, null=True)
    ingredients = models.TextField(max_length=500)
    instructions = models.TextField(max_length=500)
    imageurl = models.CharField(default=None, blank=True, max_length=300, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} added to cake #{self.cake} by user #{self.created_by}"

    class Meta:
        ordering = ['created_date']
    
    def get_absolute_url(self):
        return reverse('detail', kwargs = {'pk': self.cake_id})