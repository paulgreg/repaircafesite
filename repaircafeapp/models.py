from django.db import models
from django.forms import ModelForm


class Request(models.Model):

    name_text = models.CharField(max_length=25)
    firstname_text = models.CharField(max_length=25)
    email_text = models.CharField(max_length=40)
    phone_text = models.CharField(max_length=14)
    locality_text = models.CharField(max_length=50)

    category_text = models.CharField(max_length=16)
    object_text = models.CharField(max_length=50, blank=True)
    brand_text = models.CharField(max_length=10)
    model_text = models.CharField(max_length=15)
    year_text = models.CharField(max_length=4, blank=True)

    problem_text = models.CharField(max_length=2048)
    research_text = models.CharField(max_length=2048)
    actions_text = models.CharField(max_length=2048)
    expectation_text = models.CharField(max_length=2048)
    commitment_text = models.CharField(max_length=2048)

    reparation_day_text = models.CharField(max_length=10)

    def __str__(self):
        return self.object_text


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['name_text', 'firstname_text', 'email_text', 'phone_text', 'locality_text', 'category_text', 'object_text', 'brand_text', 'model_text',
                  'year_text', 'problem_text', 'research_text', 'actions_text', 'expectation_text', 'commitment_text', 'reparation_day_text']
