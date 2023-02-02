from django.urls import path
from .views import SendSignal, SendSignalResult

urlpatterns = [
    path('send-signal/', SendSignal.as_view(), name='send-signal'),
    path('send-signal-result/', SendSignalResult.as_view(), name='send-signal-result'),
]
