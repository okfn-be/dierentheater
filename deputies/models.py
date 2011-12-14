from django.db import models
from djangotoolbox.fields import ListField

class Deputy(models.Model):
    full_name = models.CharField(max_length=1337)
    emails = ListField()
    party = models.ForeignKey('Party')
    url = models.CharField(max_length=1337)
    websites = ListField()
    #lachambre_id = models.IntegerField(max_length=1337)
    #first_name = models.CharField(max_length=1337)
    #last_name = models.CharField(max_length=1337)

    def __unicode__(self):
        return '%s - %s' % (self.full_name, self.party)

class Party(models.Model):
    name = models.CharField(max_length=1337)
    url = models.URLField()

    def __unicode__(self):
        return self.name
