from django.db import models
from django.contrib.auth import get_user_model
import uuid



User = get_user_model()


class UserCredentials(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    phone = models.CharField(max_length=13)
    nationalno = models.IntegerField(null = True)
    idimage = models.ImageField(upload_to = 'id_photos', default='samuele-bertoli-C0gX9PFh07Q-unsplash.jpg')
    user_image = models.ImageField(upload_to = 'user_images', default='samuele-bertoli-C0gX9PFh07Q-unsplash.jpg')
    location = models.CharField(max_length = 200)
    date_created = models.DateField(auto_now_add=True)


    def __str__(self):
        return (self.first_name + ' ' + self.last_name)