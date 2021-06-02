from rest_framework import generics, status
from rest_framework.response import Response
from .serializer import (
    CourseSerializer,
    ProfessorSerializer,
    PollSerializer,
    ProfessorDataSerializer,
    GetCourseSerializer
    )
from .models import Course,Professor,Poll,ProfessorStatic


class CourseView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class ProfessorView(generics.CreateAPIView):
    serializer_class = ProfessorSerializer
    queryset = Course.objects.all()

class PollView(generics.GenericAPIView):
    serializer_class = PollSerializer

    def post(self, request):
        data = request.data

        
        if Poll.objects.filter(student=data["student"], professor=data["professor"], course=data["course"]).exists():
            return Response(
                "You have already voted.",
                status = status.HTTP_403_FORBIDDEN)
        
        if not ProfessorStatic.objects.filter(id=data["professor"], course=data["course"]).exists():
            return Response(
                "There is no course with this Professor.",
                status = status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response("Voted successful",
            status=status.HTTP_200_OK)
        
        return Response("Failed",status=status.HTTP_400_BAD_REQUEST)


class PollListView(generics.ListAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()



class ProfessorDataView(generics.ListAPIView):
    serializer_class = ProfessorDataSerializer
    queryset = Professor.objects.all()

class GetCourseView(generics.GenericAPIView):
    serializer_class = GetCourseSerializer


    def get(self, request):
        professor = request.GET.get('professor')
        course = request.GET.get('course')
        teach = 0 
        respect = 0
        for i in Poll.objects.filter(professor=professor ,course__in=course):
            teach += i.teach
            respect += i.respect
        data = {"teach" : teach, "respect": respect}
        return Response(data,status=status.HTTP_200_OK)