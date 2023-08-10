from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from .models import Train, SeatAvabilty, Compartment
from .serializers import TrainSerializer,CompartmentSerializer,SeatAvabiltySerializer


class TrainView(APIView):
    """
    Retrieve, update or delete a train instance.
    """
    def get_object(self, pk):
        try:
            return Train.objects.get(pk=pk)
        except Train.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            train = self.get_object(pk)
            serializer = TrainSerializer(train)
        else:
            train = Train.objects.all()
            serializer = TrainSerializer(train,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TrainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        train = self.get_object(pk)
        serializer = TrainSerializer(train, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        if pk:
            train = self.get_object(pk)
        else:
            train = Train.objects.all()
        train.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CompartmentView(APIView):
    """
    Retrieve, update or delete a compartment instance.
    """
    def get_object(self, pk):
        try:
            return Compartment.objects.get(pk=pk)
        except Compartment.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            comp = self.get_object(pk)
            serializer = CompartmentSerializer(comp)
        else:
            comp = Compartment.objects.all()
            serializer = CompartmentSerializer(comp,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        comp = self.get_object(pk)
        serializer = CompartmentSerializer(comp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        if pk:
            comp = self.get_object(pk)
        else:
            comp = Compartment.objects.all()
        comp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SeatAvabiltyView(APIView):
    """
    Retrieve, update or delete a seat_avability instance.
    """
    def get_object(self, pk):
        try:
            return SeatAvabilty.objects.get(pk=pk)
        except SeatAvabilty.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            seat = self.get_object(pk)
            serializer = SeatAvabiltySerializer(seat)
        else:
            seat = SeatAvabilty.objects.all()
            serializer = SeatAvabiltySerializer(seat,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SeatAvabiltySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        seat = self.get_object(pk)
        serializer = SeatAvabiltySerializer(seat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        if pk:
            seat = self.get_object(pk)
        else:
            seat = SeatAvabilty.objects.all()
        seat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

