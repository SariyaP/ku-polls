"""This module for application models."""
import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    """This module for question models."""

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField('date end', null=True, blank=True)

    def __str__(self):
        """Return question."""
        return self.question_text

    def was_published_recently(self):
        """Check if question was published recently."""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def is_published(self):
        """Check if the question is published."""
        return timezone.now() >= self.pub_date

    def can_vote(self):
        """Check if user can vote on the question."""
        if self.end_date is not None:
            if self.pub_date <= timezone.now() <= self.end_date:
                return True
            if self.end_date < self.pub_date:
                return False
            return False
        if self.end_date is None:
            return self.pub_date <= timezone.now()
        return True


class Choice(models.Model):
    """This module for choice models."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        """Return choice."""
        return self.choice_text

    @property
    def votes(self):
        """Return count of vote."""
        return self.vote_set.count()


class Vote(models.Model):
    """A vote by a user for each choice."""

    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
