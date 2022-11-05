from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from accounts.choices import ROLE_CHOICES

# Create your models here.


# ---------------------------------------------------------------------------- #
#                                  UserManager                                 #
# ---------------------------------------------------------------------------- #


class UserManager(BaseUserManager):
    """
    Creating cutome user manager
    """
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have an username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            password = password
        )
        
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
    
    
# ---------------------------------------------------------------------------- #
#                                     User                                     #
# ---------------------------------------------------------------------------- #


class User(AbstractBaseUser):
    """
    Custom User Modeal
    """
    objects = UserManager()
    
    first_name = models.CharField(
        _('First Name'),
        max_length = 100,
    )
    
    last_name = models.CharField(
        _('Last Name'),
        max_length = 100
    )
    
    username = models.CharField(
        _('Username'),
        max_length = 100,
        unique = True
    )
    
    email = models.EmailField(
        _('Email'),
        max_length = 255,
        unique = True
    )
    
    phone_number = models.CharField(
        _('Phone Number'),
        max_length = 12,
        blank = True
    )
    
    role = models.CharField(
        _('Role'),
        max_length = 20,
        choices = ROLE_CHOICES,
        null = True,
        blank = True
    )
    
    # required fields
    date_joined = models.DateTimeField(
        _('Date Joined'),
        auto_now_add = True
    )
    
    last_login = models.DateTimeField(
        _('Last Login'),
        auto_now_add = True
    )
    
    created_date = models.DateTimeField(
        _('Created Date'),
        auto_now_add = True
    )
    
    modified_date = models.DateTimeField(
        _('Modified Date'),
        auto_now = True
    )
    
    is_admin = models.BooleanField(
        _('Is Admin'),
        default = False
    )
    
    is_staff = models.BooleanField(
        _('Is Staff'),
        default = False
    )
    
    is_superadmin = models.BooleanField(
        _('Is Superadmin'),
        default = False
    )
    
    is_active = models.BooleanField(
        _('is Active'),
        default = True
    )
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name',
    ]

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    class Meta:
        ordering = ('-id', )
    
    
# ---------------------------------------------------------------------------- #
#                                  UserProfile                                 #
# ---------------------------------------------------------------------------- #


class UserProfile(models.Model):
    """
    To create user profile
    """
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )
    
    profile_picture = models.ImageField(
        _('Profile Picture'),
        upload_to = 'users/profile_pictures',
        null = True,
        blank = True
    )

    cover_picture = models.ImageField(
        _('Cover Picture'),
        upload_to = 'users/cover_picture',
        null = True,
        blank = True
    )
    
    address_line_1 = models.CharField(
        _('Address Line 1'),
        max_length = 100,
        null = True,
        blank = True,
    )
    
    address_line_2 = models.CharField(
        _('Address Line 2'),
        max_length = 100,
        null = True,
        blank = True,
    )
    
    city = models.CharField(
        _('City'),
        max_length = 50,
        null = True,
        blank = True
    )
    
    pin_code = models.CharField(
        _('Pin Code'),
        max_length = 6,
        null = True,
        blank = True
    )
    
    country = models.CharField(
        _('Country'),
        max_length = 50,
        null = True,
        blank = True
    )
    
    state = models.CharField(
        _('State'),
        max_length = 50,
        null = True,
        blank = True
    )
    
    latitude = models.CharField(
        _('Latitude'),
        max_length = 50,
        null = True,
        blank = True
    )
    
    longitude = models.CharField(
        _('Longitude'),
        max_length = 50,
        null = True,
        blank = True
    )
    
    created_on = models.DateTimeField(
        _('Created On'),
        auto_now_add = True,
        null = True,
        blank = True
    )
    
    updated_on = models.DateTimeField(
        _('Updated On'),
        auto_now = True,
        null = True,
        blank = True
    )
    
    def __str__(self):
        return str(self.user)
    
    class Meta:
        ordering = ('-id', )

    