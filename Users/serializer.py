from rest_framework import serializers
from .models import NewUser






class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    #password = serializers.CharField(required=True, write_only=True)
    session_id = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = NewUser
        fields = ('username', 'university', 'session_id')
        extra_kwargs = {'session_id' : {'write_only' : True}}
    
    def create(self, validated_data):

        #password = validated_data.pop('password', None)
        session = validated_data.pop('session_id', None)
        instance = self.Meta.model(**validated_data)
        if session is not None:
            instance.set_password(session)
        instance.save()
        return instance