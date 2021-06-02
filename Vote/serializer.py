from rest_framework import serializers
from .models import Course,Professor,Poll


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"

class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = ('course', 'name')

class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = '__all__' 


class ProfessorDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = "__all__"


class GetCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = ('teach', 'respect')