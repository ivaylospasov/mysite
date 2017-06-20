from django.db import models

# Create your models here

class Original(models.Model):
    title = models.CharField(max_length=200)
    original_text = models.TextField()
    corrected_text = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.corrected_text = self.original_text.lower()
        super(Original, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
