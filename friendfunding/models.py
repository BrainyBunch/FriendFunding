from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    amountsaved = models.IntegerField(default=0)
    
    # We should make the user i guess just be information about the person right?
    # Like email. Phone number? Bio?
    print("The User Model")
    def __str__(self):
        return self.name

class Goal(models.Model):
    title = models.CharField(max_length=100, default='none')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='goal',
    )
    description = models.TextField()
    cost = models.IntegerField(default=0)
    amountsaved = models.IntegerField(default=0)

    # Can use ForeignKey to bring in User model
    # Can also add multiple users to a specific Goal. I imagine it could do something with an array of users..
    # Would want to pull the amount saved from each user.... 
    print("The Goal Model")

    def __str__(self):
        return self.title



