from django.contrib import admin
from .models import Test, Question, TestResult, TestSeries, TestSeriesResponse
# Register your models here.
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(TestResult)
admin.site.register(TestSeries)
admin.site.register(TestSeriesResponse)
