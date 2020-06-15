from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Test(models.Model):
    class AccessType(models.IntegerChoices):
        public = 0, _('Public')
        private = 1, _('Private')
        paid = 2, _('Paid')

    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.TextField()
    duration = models.IntegerField(default=-1)
    access = models.IntegerField(default=0, choices=AccessType.choices)
    accessKey = models.TextField(default='')
    time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # remove blank and null from the production version


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


class TestResult(models.Model):
    parent_test = models.ForeignKey(Test, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.TextField()
    checked = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
