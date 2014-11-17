from django.db import models


class Parent(models.Model):
    MOM = 'mom'
    DAD = 'dad'
    GUARDIAN = 'guardian'
    ROLE_CHOICES = (
        (MOM, 'mom'),
        (DAD, 'dad'),
        (GUARDIAN, 'guardian'),
    )

    device_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=511)
    password = models.CharField(max_length=63)
    role = models.CharField(max_length=8, choices=ROLE_CHOICES, default=GUARDIAN)
    avatar = models.ImageField(null=True, default=None)

    def __unicode__(self):
        return self.name


class Kid(models.Model):
    BOY = 'boy'
    GIRL = 'girl'
    GENDER_CHOICES = (
        (BOY, 'boy'),
        (GIRL, 'girl'),
    )

    device_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    password = models.CharField(max_length=63)
    gender = models.CharField(max_length=4, choices=GENDER_CHOICES, default=BOY)
    avatar = models.ImageField(null=True, default=None)

    def __unicode__(self):
        return self.name


class Chore(models.Model):
    device_id = models.CharField(max_length=255)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    image = models.ImageField(null=True, default=None)
    custom = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name





