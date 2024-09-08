import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField('date end', null=True, blank=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def is_published(self):
        return timezone.now() >= self.pub_date

    def can_vote(self):
        if self.end_date is not None:
            if self.pub_date <=  timezone.now() <= self.end_date :
                return True
            if self.end_date < self.pub_date:
                return False
            return False
        if self.end_date is None:
            return self.pub_date <= timezone.now()
        return True

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text

    @property
    def votes(self):
        return self.vote_set.count()

class Vote(models.Model):
    """A vote by a user for each choice"""

    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)