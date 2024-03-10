from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, phone, first_name, last_name):
        email = email
        phone = phone
        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            first_name=first_name,
            last_name=last_name,
        )
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.model(
            email=self.normalize_email(email),
            is_superuser=True,
            is_staff=True,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True, blank=True)
    first_name = models.CharField(_("first name"), max_length=32, null=True, blank=True)
    last_name = models.CharField(_("last name"), max_length=32, null=True, blank=True)
    created_at = models.DateTimeField("date joined", default=timezone.now)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
