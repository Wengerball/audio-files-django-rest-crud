from django.test import TestCase
from audiofiles.models import Song, Audiobook, Podcast


class SongTest(TestCase):
    """ Test module for Song model """

    def setUp(self):
        Song.objects.create(name='Scientist', duration=300)
        Song.objects.create(name='Yellow', duration=350)

    def test_song(self):
        scientist= Song.objects.get(name='Scientist')
        yellow = Song.objects.get(name='Yellow')
        self.assertEqual(scientist.duration, 300)
        self.assertEqual(yellow.duration, 350)


class PodcastTest(TestCase):
    """ Test module for Podcast model """

    def setUp(self):
        Podcast.objects.create(name='Whats UP', duration=30000, host='Shashwat')
        Podcast.objects.create(name='All Good', duration=35000, host='Abhinav')

    def test_podcast(self):
        shashwat= Podcast.objects.get(host='Shashwat')
        all_good = Podcast.objects.get(name='All Good')
        self.assertEqual(shashwat.duration, 30000)
        self.assertEqual(all_good.host, 'Abhinav')


class AudiobookTest(TestCase):
    """ Test module for Audiobook model """

    def setUp(self):
        Audiobook.objects.create(title='Hello World', duration=300000, author='Shashwat', narrator='Akshay')
        Audiobook.objects.create(title='Footballs', duration=350000, author='Abhinav', narrator='Shubham')

    def test_audiobook(self):
        author = Audiobook.objects.get(author='Shashwat')
        title = Audiobook.objects.get(title='Footballs')
        self.assertEqual(author.title, 'Hello World')
        self.assertEqual(title.narrator, 'Shubham')