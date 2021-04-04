import json
from rest_framework import status
from django.test import TestCase, Client
from audiofiles.models import Song, Podcast, Audiobook
from audiofiles.serializers import SongSerializer, PodcastSerializer, AudiobookSerializer


client = Client()

class TestGetAllFiles(TestCase):
    """ Test module for GET all files API """

    def setUp(self):
        Song.objects.create(name='Scientist', duration=300)
        Song.objects.create(name='Yellow', duration=350)
        Podcast.objects.create(name='Whats UP', duration=30000, host='Shashwat')
        Podcast.objects.create(name='All Good', duration=35000, host='Abhinav')
        Audiobook.objects.create(
            title='Hello World', duration=300000, author='Shashwat', narrator='Akshay')
        Audiobook.objects.create(
            title='Footballs', duration=350000, author='Abhinav', narrator='Shubham')


    def test_get_all_songs(self):
        response = client.get('http://127.0.0.1:8000/api/files/?type=song')
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        self.assertEqual(response.data, serializer.data, msg=response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_get_a_song(self):
        response = client.get('http://127.0.0.1:8000/api/files/?type=song&id=1')
        song = Song.objects.get(id=1)
        serializer = SongSerializer(song)
        self.assertEqual(response.json()[0], serializer.data, msg=response.json()[0])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_get_all_podcasts(self):
        response = client.get('http://127.0.0.1:8000/api/files/?type=podcast')
        podcasts = Podcast.objects.all()
        serializer = PodcastSerializer(podcasts, many=True)
        self.assertEqual(response.data, serializer.data, msg=response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_get_a_podcast(self):
        response = client.get('http://127.0.0.1:8000/api/files/?type=podcast&id=1')
        podcast = Podcast.objects.get(id=1)
        serializer = PodcastSerializer(podcast)
        self.assertEqual(response.json()[0], serializer.data, msg=response.json()[0])
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_all_audiobooks(self):
        response = client.get('http://127.0.0.1:8000/api/files/?type=audiobook')
        audiobooks = Audiobook.objects.all()
        serializer = AudiobookSerializer(audiobooks, many=True)
        self.assertEqual(response.data, serializer.data, msg=response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_get_a_audiobook(self):
        response = client.get('http://127.0.0.1:8000/api/files/?type=audiobook&id=1')
        audiobook = Audiobook.objects.get(id=1)
        serializer = AudiobookSerializer(audiobook)
        self.assertEqual(response.json()[0], serializer.data, msg=(response.json()[0]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestCreateNewSong(TestCase):
    """ Test module for Create Song API """

    def setUp(self):
        self.valid_payload = {
            "name": "Fix You",
            "duration": 6565,
        }
        self.invalid_payload = {
            "name": "",
            "duration": "abc",
        }

    def test_create_valid_song(self):
        response = client.post(
            'http://127.0.0.1:8000/api/create/?type=song',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_song(self):
        response = client.post(
            'http://127.0.0.1:8000/api/create/?type=song',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestUpdateSinglePodcast(TestCase):
    """ Test module for updating an existing puppy record """

    def setUp(self):
        self.shashwat = Podcast.objects.create(name='Whats UP', duration=30000, host='Shashwat')
        self.abhinav = Podcast.objects.create(name='All Good', duration=35000, host='Abhinav')

        self.valid_payload = {
            "name": "Life Good",
            "duration": 7894,
            "host": "Akshay",
        }
        self.invalid_payload = {
            "name": "Life Good",
            "duration": "",
            "host": 7894,
        }


    def test_valid_update_podcast(self):
        response = client.put(
            "http://127.0.0.1:8000/api/update/?type=podcast&id={id}".format(id=self.shashwat.id),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_invalid_update_podcast(self):
        response = client.put(
            "http://127.0.0.1:8000/api/update/?type=podcast&id={id}".format(id=self.abhinav.id),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

