from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    score = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', default='2000-1-1')

    def __str__(self):
        return self.title
