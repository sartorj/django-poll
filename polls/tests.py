from django.test import TestCase

import datetime
from django.utils import timezone
from django.test import TestCase

from .models import Question

# Create your tests here.


class QuestionMethodTests(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        '''
        should be false for question whose pub_date is in future
        '''
        
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)


    def test_was_published_recently_with_recent_question(self):
        '''
        should be true when pub_date within last day
        '''
        
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(), True)


    def test_was_published_recently_with_old_question(self):
        '''
        should be true for question when pub_date within last day
        '''
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(), True)
