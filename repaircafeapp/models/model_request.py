from django.db import models
from django.forms import ModelForm
from django.db.models import Count
from django.conf import settings
from django.contrib.auth.models import User
import uuid


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    category_text = models.CharField(max_length=40)
    object_text = models.CharField(max_length=50, blank=True)
    brand_text = models.CharField(max_length=40)
    model_text = models.CharField(max_length=40)
    year_text = models.CharField(max_length=4, blank=True)
    problem_text = models.CharField(max_length=2048)
    research_text = models.CharField(max_length=2048)
    actions_text = models.CharField(max_length=2048)
    expectation_text = models.CharField(max_length=2048)
    commitment_text = models.CharField(max_length=2048)
    reparation_date = models.DateField()
    image1 = models.ImageField(upload_to='images', blank=True)
    image2 = models.ImageField(upload_to='images', blank=True)
    image3 = models.ImageField(upload_to='images', blank=True)
    image4 = models.ImageField(upload_to='images', blank=True)
    video1 = models.FileField(upload_to='videos', blank=True)
    token_text = models.CharField(max_length=32)

    def save(self, *args, **kwargs):
        self.token_text = self.token_text or uuid.uuid4().hex
        super(Request, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username + ':' + self.reparation_date.isoformat() + '->' + self.category_text


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['category_text', 'object_text', 'brand_text', 'model_text', 'year_text',
                  'problem_text', 'research_text', 'actions_text', 'expectation_text', 'commitment_text',
                  'reparation_date', 'image1', 'image2', 'image3', 'image4', 'video1']
        exclude = ('user',)


def getRequestCountByDates(token=''):
    requestsByDate = Request.objects.filter(active=True).exclude(token_text=token).values('reparation_date').annotate(
        count=Count('reparation_date')).order_by()

    return {x.get('reparation_date').isoformat(): x.get('count')
            for x in requestsByDate}


def areRequestCountFull(o):
    for x in o:
        if (x.get('places') == settings.REPAIRCAFE_MAX_SEATS):
            return False
    return True


def findByToken(token):
    return Request.objects.filter(active=True, token_text=token).first()


def findByUser(user):
    return Request.objects.filter(active=True, user=user)


def findByIdAndToken(id, token):
    return Request.objects.filter(active=True, token_text=token, id=id).first()


def getNextRequests(filterFromDate):
    return Request.objects.filter(active=True, reparation_date__gte=filterFromDate.date().isoformat()).order_by('reparation_date')
