from django.db import models
from django.urls import reverse

class PasswordInstance(models.Model):
    # username
    user = models.CharField(max_length=200)
    # password title
    title = models.CharField(max_length=200)
    # password description
    description = models.TextField(max_length=2000)

    # password 
    password = models.CharField(max_length=32, blank=True)
    # or
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('pass_detail', args=[str(self.id)])