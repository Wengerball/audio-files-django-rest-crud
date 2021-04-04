from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from audiofiles.models import Song, Audiobook, Podcast
from audiofiles.serializers import SongSerializer, AudiobookSerializer, PodcastSerializer


class FileList(generics.ListAPIView):
    serializer_class = SongSerializer

    def get_queryset(self):
        try:
            file_type = self.request.query_params.get("type", None)
            print(file_type)
            file_id = self.request.query_params.get("id", None)
            model_type_dict = {
                'song': Song,
                'podcast': Podcast,
                'audiobook': Audiobook
            }
            model = model_type_dict[file_type]
            queryset = model.objects.all()
            if file_id:
                queryset = queryset.filter(id=file_id)
            if not queryset:
                return None
            return queryset
        except:
            return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)


    def list(self, request):
        try:
            queryset = self.get_queryset()
            if queryset.model.__name__ == 'Song':
                serializer_class = self.get_serializer(queryset, many=True)
            elif queryset.model.__name__ == 'Podcast':
                serializer_class = PodcastSerializer(queryset, many=True)
            else:
                serializer_class = AudiobookSerializer(queryset, many=True)
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        except:
            return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)


class FileDelete(generics.DestroyAPIView):
    def get_object(self):
        try:
            file_type = self.request.query_params.get("type", None)
            file_id = self.request.query_params.get("id", None)
            model_type_dict = {
                'song': Song,
                'podcast': Podcast,
                'audiobook': Audiobook
            }
            model = model_type_dict[file_type]
            queryset = model.objects.get(id=file_id)
            if not queryset:
                return None
            return queryset
        except:
            return None

    def destroy(self, request):
        try:
            instance = self.get_object()
            instance.delete()
            return Response("Object Deleted", status=status.HTTP_200_OK)
        except:
            return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)


class FileCreate(generics.CreateAPIView):
    serializer_class = SongSerializer

    def create(self, request):
        try:
            file_type = self.request.query_params.get("type", None)
            data=request.data
            print(data)
            print(file_type)
            if file_type == 'song':
                serializer_class = self.get_serializer(data=data)
                serializer_class.is_valid(raise_exception=True)
                serializer_class.save() 

            elif file_type == 'podcast':
                serializer_class = PodcastSerializer(data=data)
                serializer_class.is_valid(raise_exception=True)
                serializer_class.save() 
            else:
                serializer_class = AudiobookSerializer(data=data)
                serializer_class.is_valid(raise_exception=True)
                serializer_class.save() 
            return Response("Object Created", status=status.HTTP_200_OK)
        except:
            return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)


class FileUpdate(generics.UpdateAPIView):
    serializer_class = SongSerializer

    def update(self, request):
        try:
            file_type = self.request.query_params.get("type", None)
            file_id = self.request.query_params.get("id", None)
            data = request.data
            if file_type == 'song':
                id = Song.objects.get(id=file_id)
                serializer_class = self.get_serializer(id, data=data)
                serializer_class.is_valid(raise_exception=True)
                serializer_class.save() 

            elif file_type == 'podcast':
                id = Podcast.objects.get(id=file_id)
                serializer_class = PodcastSerializer(id, data=data)
                serializer_class.is_valid(raise_exception=True)
                serializer_class.save() 
            else:
                id = Audiobook.objects.get(id=file_id)
                serializer_class = AudiobookSerializer(id, data=data)
                serializer_class.is_valid(raise_exception=True)
                serializer_class.save() 
            return Response("Object Updated", status=status.HTTP_200_OK)
        except:
            return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)
