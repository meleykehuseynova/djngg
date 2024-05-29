from django.db import models

# Create your models here.
class site(models.Model):
    post_sahibi=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    basliq=models.CharField(max_length=100)
    post=models.TextField()
    yaranma_tarixi=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.basliq
