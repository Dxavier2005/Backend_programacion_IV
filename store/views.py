from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventoSerializer

class EventoListAPIView(APIView):
    def get(self, request):
        eventos = Event.objects.all()
        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventoDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return None

    def get(self, request, pk):
        evento = self.get_object(pk)
        if not evento:
            return Response({"error": "No encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EventoSerializer(evento)
        return Response(serializer.data)

    def put(self, request, pk):
        evento = self.get_object(pk)
        if not evento:
            return Response({"error": "No encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EventoSerializer(evento, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        evento = self.get_object(pk)
        if not evento:
            return Response({"error": "No encontrado"}, status=status.HTTP_404_NOT_FOUND)
        evento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)