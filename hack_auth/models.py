from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        """
        self..............(self) The instance to be executed against.
        username..........(username, required) The registered name of the user.
        email.............(email, required) The registered email of the user.
        password..........(password, required) The registered password of the user.
        """
        
        if username is None:
            raise TypeError("User must have username")
        if email is None:
            raise type("User must have email")
        
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, password=None):

        if password is None:
            raise TypeError("Password should not be none")
        
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
    
class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self) -> str:
        return self.email
    
    def token(self):
        pass