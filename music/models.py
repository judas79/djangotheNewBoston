from django.db import models

# Create your models here.


# inherited fom models.Model
class Album(models.Model):

    # what variables would exist in a Album, 'artist'
    # what kind of data is being stored in it, text  'CharField'
    # One field required size 'max_length'
    artist = models.CharField(max_length=250)      # <-  column 1 ....
    album_title = models.CharField(max_length=450)
    genre = models.CharField(max_length=150)
    # max length large to accommodate a url link
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):

    # to link this Song class to the Album class using ForeignKey
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_types = models.CharField(max_length=10)
    song_title = models.CharField(max_length=100)
    # added lesson 22, to link attribute is-favorite to radio buttons to mark favorite songs
    is_favorite = models.BooleanField(default=False)
    # added lesson 17
    def __str__(self):
        return self.song_title

