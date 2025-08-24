from django.db import models

# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.caption if self.caption else "Photo"

class Video(models.Model):
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.caption if self.caption else "Video"