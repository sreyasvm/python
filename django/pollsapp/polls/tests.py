import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Question

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_date(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        future_date = timezone.now() + datetime.timedelta(days=20)
        future_question = Question(pub_date = future_date)
        self.assertIs(future_question.was_published_recently(),False)






