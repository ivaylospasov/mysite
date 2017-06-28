from django.db import models

# Create your models here

class NewsText(models.Model):
    title = models.CharField(max_length=200)
    original_text = models.TextField()

    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        super(NewsText, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
