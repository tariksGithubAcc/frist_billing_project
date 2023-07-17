from django.db import models

class SMSMessage(models.Model):
    content = models.TextField()
    recipient = models.CharField(max_length=100)
    sender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
