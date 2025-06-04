from django.db import models
from django.contrib.auth.models import User

class Server(models.Model):
    name = models.CharField(max_length=255)
    ip = models.GenericIPAddressField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='servers')

    def __str__(self):
        return self.name

class Promotion(models.Model):
    PROMO_TYPES = [
        ('highlight', 'Highlight'),
        ('top', 'Top'),
        ('pin', 'Pin'),
        ('featured', 'Featured'),
    ]
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='promotions')
    type = models.CharField(max_length=20, choices=PROMO_TYPES)
    expires_at = models.DateTimeField()
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-expires_at']

    def __str__(self):
        return f'{self.server} - {self.type}'