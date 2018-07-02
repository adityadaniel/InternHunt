from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "cities"

    def __str__(self):
        return self.name

class Internship(models.Model):
    position = models.CharField(max_length=150)
    source = models.URLField(max_length=150)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.ForeignKey(City, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} @ {1}".format(self.position, self.company)
