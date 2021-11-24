from django.db import models


class Name(models.Model):
    id = models.AutoField(primary_key=True)
    input_name = models.CharField(max_length=20)

    def __str__(self):
        return self.input_name

