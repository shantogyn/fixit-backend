from django.db import models

# Create your models here.
class Service(models.Model):
    id = models.AutoField(primary_key=True)
    provider_id = models.IntegerField()
    category_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='inactive')
    created_at = models.DateTimeField(auto_now_add=True)
    service_image = models.ImageField(upload_to='service_images/', null=True, blank=True)

    def __str__(self):
        return self.title