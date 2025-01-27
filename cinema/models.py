from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return str(self.title)
