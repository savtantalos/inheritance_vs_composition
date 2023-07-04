import json
import xml.etree.ElementTree as et
from typing import Callable


class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:
    def serialize(self, song: Song, formats):
        serializers: Callable = self._get_serializer(formats)
        return serializers(song)

    def _get_serializer(self, formats):
        if formats == 'JSON':
            return self._serialize_to_json
        elif formats == 'XML':
            return self._serialize_to_xml
        else:
            raise ValueError(formats)

    @staticmethod
    def _serialize_to_json(song: Song):
        payload = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(payload)

    @staticmethod
    def _serialize_to_xml(song: Song):
        song_info = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_info, 'title')
        title.text = song.title
        artist = et.SubElement(song_info, 'artist')
        artist.text = song.artist
        return et.tostring(song_info, encoding='unicode')


song = Song('1', 'Water of Love', 'Dire Straits')
serializer = SongSerializer()
print(serializer.serialize(song, 'JSON'))
