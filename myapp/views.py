from .models import Client, Mailinglist, Messagetosend
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import ClientSerializer, MailinglistSerializer,StatisticsSerializer
#, MessagetosendSerializer







class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Client.objects.all().order_by('id')
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]


class MalingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows mailinglists to be viewed or edited.
    """
    queryset = Mailinglist.objects.all().order_by('id')
    serializer_class = MailinglistSerializer
    permission_classes = [permissions.IsAuthenticated]




class StatViewSet(viewsets.ModelViewSet):
    """
    получения статистики по созданным рассылкам
     и количеству отправленных сообщений по ним с группировкой по статусам

     отправленные sent_msg
     не отправленные unsent_msg
     сообщения all_msg

    """

    queryset = Mailinglist.objects.all().order_by('id')
    serializer_class = StatisticsSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'head']