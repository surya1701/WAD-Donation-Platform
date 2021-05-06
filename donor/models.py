from django.db import models

# Create your models here.


class Users(models.Model):
    # user_id = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False)
    # autofield
    email = models.EmailField()
    total_amt = models.PositiveIntegerField(default=0)
    since = models.DateTimeField(auto_now_add=True)


class Causes(models.Model):
    cause = models.CharField(max_length=50)
    ngo_name = models.CharField(max_length=50)
    amount_req = models.PositiveIntegerField()
    amount_donated = models.PositiveIntegerField(default=0)
    image = models.URLField(default="static/images/index/img-4.jpg")


class Donations(models.Model):
    cause_id = models.ForeignKey(Causes, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    razorpay_id = models.CharField(unique=True, max_length=50)
    paid = models.BooleanField(default=False)
