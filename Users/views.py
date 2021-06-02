from rest_framework import generics,status
from .serializer import UserSerializer
from rest_framework.response import Response



class RegisterationView(generics.GenericAPIView):

    serializer_class = UserSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

