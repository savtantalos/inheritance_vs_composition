import yaml
import serializer_classes

class YamlSerializer(serializer_classes.JsonSerializer):
    def to_str(self):
        return yaml.dump(self._current_object)
serializer_classes.factory.register_format('YAML', YamlSerializer)