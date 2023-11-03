from django.db import models
from django.contrib.auth.models import User

class Suv(models.Model):
    brend = models.CharField(max_length=150)
    narx = models.PositiveBigIntegerField()
    litr = models.PositiveBigIntegerField()
    batafsil = models.TextField()

    def __str__(self):
        return self.brend

class Mijoz(models.Model):
    ism = models.CharField(max_length=150)
    tel = models.CharField(max_length=15)
    manzil = models.CharField(max_length=500)
    qarz = models.PositiveBigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism

class Admin(models.Model):
    ism = models.CharField(max_length=150)
    yosh = models.PositiveIntegerField()
    ish_vaqti = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"admin: {self.ism}"

class Haydovchi(models.Model):
    ism = models.CharField(max_length=150)
    tel = models.CharField(max_length=15)
    kiritilgan_sana = models.DateField(auto_now_add=True)

class Buyurtma(models.Model):
    suv = models.ForeignKey(Suv, on_delete=models.CASCADE)
    date = models.DateField()
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    miqdor = models.PositiveBigIntegerField()
    narx = models.PositiveBigIntegerField()
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    haydovchi = models.ForeignKey(Haydovchi, on_delete=models.CASCADE)

    def __str__(self):
        return f"buyurtma: {self.miqdor}litr"





