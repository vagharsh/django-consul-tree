from django.db import models


class Consul(models.Model):
    title = models.CharField(max_length=60)
    url = models.CharField(max_length=120)
    token = models.CharField(max_length=90)

    def __str__(self):
        return self.title
