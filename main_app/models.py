from django.db import models
from django.urls import reverse


PRACTICE = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)
# Create your models here.

class Suit(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('suits_details', kwargs={'pk': self.id})

class Power(models.Model):
    name = models.CharField(max_length=100)
    weakness = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    level = models.IntegerField()
    suits = models.ManyToManyField(Suit)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details', kwargs={'power_id': self.id})

class Training(models.Model):
    date = models.DateField('training date')
    practice = models.CharField(
        max_length=1,
        choices=PRACTICE,
        default=PRACTICE[0][0]
    )
    power = models.ForeignKey(Power, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_practice_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    power = models.ForeignKey(Power, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for power_id: {self.power_id} @{self.url}"

