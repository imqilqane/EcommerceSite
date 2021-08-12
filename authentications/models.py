from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManagaer(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('A user has to have an username')
        if not email:
            raise ValueError('A user has to have an email')

        user = self.model(
            email = self.normalize_email(email),
            username = username
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):

    def get_profile_picture_path(self):
        return f'profiles/{self.id}'

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_image = models.ImageField(
        upload_to=get_profile_picture_path, null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined',
        auto_now=True)
    last_login = models.DateTimeField(verbose_name='last login',
        auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    objects = UserManagaer()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True