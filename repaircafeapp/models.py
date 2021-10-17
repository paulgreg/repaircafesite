from django.db import models
from django.forms import ModelForm
from django.db.models import Count
import uuid


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
    reparation_date = models.DateField()
    token_text = models.CharField(max_length=32)

    def save(self, *args, **kwargs):
        self.token_text = self.token_text or uuid.uuid4().hex
        super(Request, self).save(*args, **kwargs)

    def __str__(self):
        return self.reparation_date.isoformat() + '->' + self.category_text


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['name_text', 'firstname_text', 'email_text', 'phone_text', 'locality_text', 'category_text', 'object_text', 'brand_text', 'model_text',
                  'year_text', 'problem_text', 'research_text', 'actions_text', 'expectation_text', 'commitment_text', 'reparation_date']


def getRequestCountByDates(token=''):
    requestsByDate = Request.objects.exclude(token_text=token).values('reparation_date').annotate(
        count=Count('reparation_date')).order_by()

    return {x.get('reparation_date').isoformat(): x.get('count')
            for x in requestsByDate}


def findByToken(token):
    return Request.objects.filter(token_text=token).first()


def findByIdAndToken(id, token):
    return Request.objects.filter(token_text=token, id=id).first()


def getNextRequests(filterFromDate):
    return Request.objects.filter(reparation_date__gte=filterFromDate.date().isoformat()).order_by('reparation_date')
