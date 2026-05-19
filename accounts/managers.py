from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email, name and password.
        """
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name
        )
        user.set_password(password)
        user.save()
        return user

    def create_renter(self, email, name, password=None):
        """
        Creates and saves a rentor with the given email, name and password.
        """
        user = self.create_user(
            email,
            name,
            password=password,
        )
        user.is_renter = True

        user.save()
        return user

    def create_superuser(self, email, name, password=None):
        """
        Creates and saves a superuser with the given email, name and password.
        """
        user = self.create_user(
            email,
            name,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
