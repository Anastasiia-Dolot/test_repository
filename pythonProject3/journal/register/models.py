from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(verbose_name='Фото', default='default.png', upload_to='user_images')

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super().save()
        image = Image.open(self.img.path)
        if image.width > 80 or image.height > 80:
            resize = (80, 80)
            image.thumbnail(resize)
            image.save(self.img.path)
            return image

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = 'Профили'