from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title