import json
import xml.etree.ElementTree as et
from spotify.my_song import Song
from abc import ABC, abstractmethod


class Serializer:

    @abstractmethod
    def start_object(self, object_name, object_id):
        """initiate the obect which we will serialize"""

    def add_element(self, element, value):
        """will add a key:element and its related value:value"""

    def to_str(self):
        """will output the format that we want"""


class JsonSerializer(Serializer):

    def __init__(self):
        self._config = dict()

    def start_object(self, object_name: str, object_id: str):
        self._config[object_name] = object_id

    def add_element(self, element, value):
        self._config[element] = value

    def to_str(self):
        return json.dumps(self._config)


class XmlSerializer(Serializer):

    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = et.Element(object_name, attrib={'id': object_id})

    def add_element(self, name, value):
        prop = et.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return et.tostring(self._element, encoding='unicode')


class SerializeFactory:
    def __init__(self):
        self._creator = dict()

    def register_format(self, format, serializer_method):
        self._creator[format] = serializer_method

    def get_serializer(self, format):
        creator = self._creator.get(format)
        if not creator:
            raise ValueError(format)
        return creator()


class ObjectSerializer:
    config = {'JSON':JsonSerializer(),
              'XML':XmlSerializer()

    }
    def serialize(self, serializable: Song, format: str):
        serializer = factory.get_serializer('JSON')
        serializable.serialize(serializer)
        return serializer.to_str()


factory = SerializeFactory()
factory.register_format('JSON', JsonSerializer)
factory.register_format('XML', XmlSerializer)

song = Song(1,'Let the night away', 'Savvas')
x = ObjectSerializer().serialize(song,'JSON')
print(x)
#print(ObjectSerializer().serialize(song,'JSON'))
