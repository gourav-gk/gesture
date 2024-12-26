from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class SharedImage(models.Model):
    image_name = models.CharField(max_length=255)  # Store the image name
    user_ip = models.GenericIPAddressField()  # Store the user's IP address
    shared_at = models.DateTimeField(auto_now_add=True)  # Store the timestamp of the action

    def __str__(self):
        return f"{self.image_name} shared by {self.user_ip} on {self.shared_at}"
