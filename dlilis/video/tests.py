import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Video
# Create your tests here.


class VideoMethodTests(TestCase):
    def test_was_published_recently_with_return_question(self):
        '''
        :return:
        '''
