from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Profile(models.Model):
    class Email_Verification(models.IntegerChoices):
        verified = 1
        not_verified = 0

    class Type(models.TextChoices):
        student = 'S', _('student')
        instructor = 'I', _('instructor')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        default='users/profile_pic/default.jpg', upload_to='users/profile_pic')
    DOB = models.DateField(blank='true', null='true')
    email_verified = models.IntegerField(
        choices=Email_Verification.choices, default=0)
    type = models.CharField(max_length=12, default='S', choices=Type.choices)

    def __str__(self):
        return f'{self.user.first_name} Profile'


@receiver(post_save, sender=User)
def profileCreate(sender, **kwargs):
    if(kwargs['created']):
        prof = Profile.objects.create(user=kwargs['instance'])
        prof.save()
