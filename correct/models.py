from django.db import models

# Create your models here

class Original(models.Model):
    title = models.CharField(max_length=200)
    original_text = models.TextField()

    def __str__(self):
        return self.title
