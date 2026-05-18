from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def generate_uuid():
    import uuid
    return uuid.uuid4()

class UserProfile(models.Model):
    uuid = models.UUIDField(primary_key=True ,default=generate_uuid, editable=False)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the international format."
            )
        ]
    )
    display_name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to = 'profiles/',
        blank=True,
        null=True,
        validators=[val_pic_size]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.display_name:
            self.display_name = self.user.username
        normalize_uploaded_image(self.profile_picture, (512, 512))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.display_name or self.user.username
