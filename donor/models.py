from django.db import models

# Create your models here.


class Users(models.Model):
    # user_id = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False)
    # autofield
    email = models.EmailField()
    total_amt = models.PositiveIntegerField(default=0)
    since = models.DateTimeField(auto_now_add=True)
