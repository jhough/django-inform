from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)

    def __unicode__(self):      # Python 3: def __str__(self):
        return '%s' % self.title