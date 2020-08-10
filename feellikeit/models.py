from django.db import models
from django.utils import timezone
# Create your models here.


class FeelLikeIt(models.Model):
    date = models.DateTimeField(default=timezone.now)
    reason = models.TextField(default="Maybe it's just too boring.")
    snap = models.ImageField(upload_to='snap', default='/pics/never_mind.png')
    no = models.TextField(default="Just simply don't do that.")

    def __str__(self):
        return str(self.date)


