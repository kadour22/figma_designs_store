from django.db import models
from django.contrib.auth.models import User

class Project(models.Model) :
    name = models.CharField(max_length=255)
    descriptions = models.TextField()
    prototype_url = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)

class ProjectImage(models.Model) :
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    project = models.ForeignKey(Project , on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.created_at

class Wishlist(models.Model) :
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="wishlist")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f"{self.project.name} wishlisted by {self.user.username}"