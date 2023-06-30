from rest_framework import generics
from .models import Table, Booking
from .serializers import TableSerializer, BookingSerializer


class TableView(generics.ListAPIView):
    serializer_class = TableSerializer

    def get_queryset(self):
        datetime_str = self.request.query_params.get('datetime')
        if datetime_str:
            return Table.objects.exclude(booking__datetime=datetime_str)
        return Table.objects.all()


class BookingView(generics.CreateAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        return Booking.objects.all()

    def perform_create(self, serializer):
        datetime_str = self.request.data.get('datetime')
        table_id = self.request.data.get('table')
        table = Table.objects.get(pk=table_id)
        serializer.save(table=table, datetime=datetime_str)
