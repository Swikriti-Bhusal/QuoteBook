from django.db import models
# Create your models here.
class Quote(models.Model):
    title = models.CharField(max_length=100)  # The quote text itself
    author = models.CharField(max_length=100, blank=True, null=True)  # Optional author name
    image = models.ImageField(upload_to='quotes_images/', blank=True, null=True)  # Image for the quote
    description=models.CharField(max_length=500)
    def __str__(self):
        return f'"{self.title}" - {self.author}'
    
