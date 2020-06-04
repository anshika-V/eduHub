from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Test(models.Model):
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.TextField()


class Question(models.Model):
    class typeChoice(models.TextChoices):
        descriptive = 'D', _("Descriptive")
        oneOption = 'O', _('One_Option_Correct')
        multiOption = 'M', _('Multu_Option_Correct')
        fill = 'F', _('Fill')
    parent_test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.TextField()
    type = models.CharField(max_length=1, choices=typeChoice.choices)
    image = models.ImageField(
        upload_to='material/question', blank=True, null=True)
    answer = models.TextField(blank=True)
    marks = models.IntegerField(default=0)
    jsonChoices = models.TextField(blank=True)
