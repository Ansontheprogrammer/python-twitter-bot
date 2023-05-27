from django.db import models

# Create your models here.
class User(models.Model):
    # Identify the user by their device's IP address
    ip_address = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    created_date = models.DateTimeField("created date")
    


class Prompt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt_text = models.CharField(max_length=1000)
    created_date = models.DateTimeField("created date")
    def __str__(self):
        return self.prompt_text
    
class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=300)
    created_date = models.DateTimeField("created date")
    def __str__(self):
        return self.message_text
