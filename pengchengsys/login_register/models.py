from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, user_name, phone_num, password=None):
        """
        Creates and saves a User with the given name, phone number and password.
        """
        if not user_name:
            raise ValueError('Users must have a name!')

        user = self.model(
            user_name=user_name,
            phone_num=phone_num,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, phone_num, password):
        """
        Creates and saves a superuser with the given name, phone number and password.
        """
        user = self.create_user(
            user_name=user_name,
            phone_num=phone_num,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    user_name = models.CharField(max_length=128)
    phone_num = models.BigIntegerField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['phone_num']

    def __str__(self):
        return self.user_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
