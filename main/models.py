from django.db import models
from django.contrib.postgres.fields import JSONField


class FormDataModel(models.Model):
    form_data = JSONField()

    def __str__(self):
        return str(self.id)
