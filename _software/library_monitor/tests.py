from django.test import TestCase

# Suite of test cases to test functionality and edge cases of FLOM web app
# Create your tests here.

import datetime

from django.test import TestCase
from django.utils import timezone

from database.models import Log, Room, Occupy


# class QuestionModelTests(TestCase):

#     def test_was_published_recently_with_future_question(self):
#         """
#         was_published_recently() returns False for questions whose pub_date
#         is in the future.
#         """
#         time = timezone.now() + datetime.timedelta(days=30)
#         future_question = Question(pub_date=time)
#         self.assertIs(future_question.was_published_recently(), False)