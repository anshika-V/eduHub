# Generated by Django 3.0.6 on 2020-06-23 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default='user/profile_pic/default.jpg', upload_to='user/profile_pic')),
                ('DOB', models.DateField(blank='true', null='true')),
                ('email_verified', models.IntegerField(choices=[(1, 'Verified'), (0, 'Not Verified')], default=0)),
                ('type', models.CharField(choices=[('S', 'student'), ('I', 'instructor')], default='S', max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
