from rest_framework.response import Response
from rest_framework import generics, status
from .models import Signal, SignalResult

# http://127.0.0.1:8000/api/send-signal/?name=TESTUSDT&type=LONG&price=13456&source=TrSc


class SendSignal(generics.RetrieveAPIView):
    queryset = Signal.objects.all()

    def retrieve(self, request, *args, **kwargs):
        name = request.query_params.get('name')
        signal_type = request.query_params.get('type')
        price = request.query_params.get('price')
        source = request.query_params.get('source')
        signal = Signal.objects.create(
            name=name,
            type=signal_type,
            price=price,
            source=source,
        )
        return Response(f"signal - {signal.id}", status=status.HTTP_200_OK)


class SendSignalResult(generics.RetrieveAPIView):
    queryset = SignalResult.objects.all()

    def retrieve(self, request, *args, **kwargs):
        name = request.query_params.get('name')
        signal_type = request.query_params.get('type')
        price = request.query_params.get('price')
        source = request.query_params.get('source')
        price_change = request.query_params.get('price_change')
        signal_result = SignalResult.objects.create(
            name=name,
            type=signal_type,
            price=price,
            source=source,
            price_change=price_change,
        )
        return Response(f"signal - {signal_result.id}", status=status.HTTP_200_OK)
