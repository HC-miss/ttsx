# Generated by Django 2.0.7 on 2018-09-13 01:41

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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(blank=True, max_length=20, null=True, verbose_name='电话')),
                ('img', models.ImageField(blank=True, null=True, upload_to='userimg/', verbose_name='用户头像')),
                ('org', models.CharField(max_length=20, verbose_name='职业')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '个人信息',
            },
        ),
    ]
