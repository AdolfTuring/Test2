from rest_framework import serializers

class FunctionSerilizer(serializers.Serializer):
    data=serializers.ListField()
    rule=serializers.ListField()
    