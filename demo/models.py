from django.db import models


class Picture(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title
