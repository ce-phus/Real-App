from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must rovide a valid email address"))
        
        def create_user(
                self, username, first_name, last_name, email, password, **extra_fields
        ):
            if not username:
                raise ValueError(_("Users must submit a username"))
            
            if not first_name:
                raise ValueError(_("Users must submit a first name"))
            
            if not last_name:
                raise ValueError(_("Users must submit a last name"))
            
            if email:
                email = self.normalize_email(email)
                self.email_validator(email)
            else:
                raise ValueError(_("Base User Account: An email address is required"))
            
            # user  = self.model(
            #     username=username
            #     first_name=first_name
            #     last_name=last_name
            #     email=email
            #     **extra_fields
            # )
            # user.set_pass

