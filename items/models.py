from django.db import models
from django.contrib.auth.models import User
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=255)
    image_b64_addr = models.TextField()
    description = models.TextField()
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=60, default="unsold")
    best_before_date = models.DateField(auto_now_add=False, auto_now=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
