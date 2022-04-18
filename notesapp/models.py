from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Notes(models.Model):
    TAGS = (
        ("work", "WORK"),
        ("recipes", "RECIPES"),
        ("sports", "SPORTS"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    desciption = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    tags = models.CharField(max_length=50, choices=TAGS)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['tags']
