from django.db import models

PERMISSION = (
    ("user", "User"),
    ("staff", "Staff"),
    ("superuser", "Superuser"),
)

#----------------------------------------------------------------------------

class Account(models.Model):
      '''General user details'''
      first_name = models.CharField(max_length=50)
      last_name = models.CharField(max_length=50)
      phone = models.CharField(max_length=100, null=True, blank=True, unique=True)
      email = models.EmailField(blank=False, null=False, unique=True)
      password = models.CharField(max_length=200, blank=False, null=False)

      def __str__(self):
            return f"Name: {self.first_name} {self.last_name} | Email: {self.email}"

#----------------------------------------------------------------------------

class AccountExtention(models.Model):
      '''Extention of "Account Model"'''
      account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
      # phone_verification_link = models.TextField(null=True, blank=True)
      token_email = models.CharField(max_length=200, null=True, blank=True)
      # token_phone = models.CharField(max_length=200, null=True, blank=True)
      changepass_uid = models.CharField(max_length=200, null=True, blank=True)
      email_is_verified = models.BooleanField(default=False)
      # phone_is_verified = models.BooleanField(default=False)
      permission = models.CharField(max_length=20, choices=PERMISSION, null=True, default="User")
      created_at = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return f"{self.account.email} | {'Email Verified' if self.email_is_verified else 'Unverified'}"

#----------------------------------------------------------------------------