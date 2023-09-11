from config.common.base.models import BaseModel

from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser, BaseModel):
    email = models.EmailField(
        verbose_name="email",
        max_length=256,
        unique=True,
        validators=[EmailValidator("이메일 주소가 올바르지 않습니다. @와 .을 포함해주세요.")],
    )
    password = models.CharField(
        verbose_name="password", 
        max_length=128
    )
    phone_number = models.CharField(
        verbose_name="phone number", 
        max_length=128
    )
    device_uuid = models.CharField(
        verbose_name="device identifier", 
        max_length=128
    )
    is_admin = models.BooleanField(
        "administrator or not", 
        default=False
    )
    is_active = models.BooleanField(
        "login or not", 
        default=True
    )