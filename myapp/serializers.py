from .models import Client, Mailinglist, Messagetosend
from rest_framework import serializers


class ClientSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Client
		fields = ['id', 'phone_number','operator_code', 'tag', 'timezone']
		read_only_fields = ('id','operator_code')



class MailinglistSerializer(serializers.HyperlinkedModelSerializer):
	datetime_start = serializers.DateTimeField()
	datetime_end = serializers.DateTimeField()
	class Meta:
		model = Mailinglist
		fields = ['id', 'datetime_start', 'message_text', 'datetime_end', 'filter_tag', 'filter_op_codes']





class StatisticsSerializer(serializers.HyperlinkedModelSerializer):

	sent_msg = serializers.SerializerMethodField(read_only=True)
	unsent_msg = serializers.SerializerMethodField(read_only=True)
	all_msg = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = Mailinglist
		fields = ['id', 'datetime_start', 'message_text', 'datetime_end', 'filter_tag', 'filter_op_codes', 'sent_msg','unsent_msg', 'all_msg']

	def get_sent_msg(self, obj):
		return Messagetosend.objects.filter(context_part=obj.id, is_sent=True).count()

	def get_unsent_msg(self, obj):
		return Messagetosend.objects.filter(context_part=obj.id, is_sent=False).count()

	def get_all_msg(self,obj):
		return Messagetosend.objects.filter(context_part=obj.id).values()