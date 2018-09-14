from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField('电话', max_length=20, blank=True, null=True)
    img = models.ImageField('用户头像', upload_to='userimg/', null=True, blank=True)
    org = models.CharField('职业', max_length=20)

    class Meta:
        verbose_name_plural = '个人信息'

    def __str__(self):
        return self.user.__str__()
