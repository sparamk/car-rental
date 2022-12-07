from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    feedback_text = models.TextField()
    feedback_date = models.DateTimeField(auto_now_add=True)