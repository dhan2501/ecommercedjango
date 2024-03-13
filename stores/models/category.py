from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    # Show caytegory name in product list admin dashboard
    def __str__(self):
        return self.name
