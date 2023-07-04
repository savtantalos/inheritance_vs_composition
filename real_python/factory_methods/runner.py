from real_python.factory_methods import song
import serializer_classes

song = song.Song('1', 'Water of Love', 'Dire Straits')
serializer = serializer_classes.ObjectSerializer()
serializer.serialize(song, 'JSON')