from django.db import models

class Star(models.Model):
    """ Звезда безопасности """
    value = models.SmallIntegerField("Значение",default=0)
    def __str__(self):
        return f'{self.value}'
    class Meta:
        verbose_name = "Звезда"
        verbose_name_plural = "Звезды"

class Image(models.Model):
    image = models.ImageField("Фото",upload_to="sharing_images/")

class Sharing(models.Model):
    """ Сама парковка """
    name = models.CharField("Название", max_length=150)
    companyname = models.CharField("Название", max_length=150)
    places = models.SmallIntegerField("Количество мест", default=0)
    price = models.IntegerField("Цена", default=0);
    goodprices = models.CharField("За:",max_length=120, default="Км")
    sitelink = models.CharField("Ссылка на сайт",max_length=220, default=None);
    latitude = models.FloatField("Широта")
    longitude = models.FloatField("Долгота")
    images =models.ForeignKey(Image,on_delete=models.CASCADE,default=1)
    safetystar = models.ForeignKey(Star, on_delete=models.CASCADE,verbose_name="Звезда безопасности",default=None)
    def __str__(self):
        return self.name



# Create your models here.
