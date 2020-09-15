from django.db import models

class SafetyStar(models.Model):
    """ Звезда безопасности """
    value = models.SmallIntegerField("Значение",default=0)
    def __str__(self):
        return f'{self.value}'
    class Meta:
        verbose_name = "Звезда безопасности"
        verbose_name_plural = "Звезды безопасности"

class ComfortStar(models.Model):
    """ Звезда безопасности """
    value = models.SmallIntegerField("Значение",default=0)
    def __str__(self):
        return f'{self.value}'
    class Meta:
        verbose_name = "Звезда комфорта"
        verbose_name_plural = "Звезды комфорта"

class Image(models.Model):
    image = models.ImageField("Фото",upload_to="parking_images/")

class Parking(models.Model):
    """ Сама парковка """
    name = models.CharField("Название", max_length=150)
    places = models.SmallIntegerField("Количество мест", default=0)
    latitude = models.FloatField("Широта")
    longitude = models.FloatField("Долгота")
    images =models.ForeignKey(Image,on_delete=models.CASCADE,default=1)
    safetystar = models.ForeignKey(SafetyStar, on_delete=models.CASCADE,verbose_name="Звезда безопасности",default=None)
    comfortstar = models.ForeignKey(ComfortStar, on_delete=models.CASCADE,verbose_name="Звезда Комфорта",default=None)

    def __str__(self):
        return self.name

