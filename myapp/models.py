from django.db import models
from django.core.validators import RegexValidator
from pytz import common_timezones
import re
from datetime import datetime 
from django.utils import timezone 


class Client(models.Model):
	#номер телефона клиента в формате 7 xxx xxx xx xx (X - цифра от 0 до 9)
	phone_number = models.CharField(max_length=11, unique=True, validators=[RegexValidator(r'^7\d{10}')])   
	#код мобильного оператора в формате XXX
	# только валидные (РФ) коды оператора (900-999) r'\9\d{2}/'
	# любой код (000-999) r'\d{3}'
	operator_code = models.CharField(max_length=3, validators=[RegexValidator(r'^9\d{2}')])
	tag = models.CharField(max_length=255,  null=True, blank=True)
	# pytz.common_timezones http://pytz.sourceforge.net/#helpers
	timezone = models.CharField(max_length=32, choices=[(tz, tz) for tz in common_timezones], 
    default='UTC')
	# override save method to auto-parse operator code from phone number
	def save(self, *args, **kwargs):
		self.operator_code = self.phone_number[1:4]
		x = re.search("^9\d{2}", str(self.operator_code))
		if x:
			super(Client, self).save(*args, **kwargs)
		else:
			raise ValidationError('invalid operator_code not in (900-999) range')



class Mailinglist(models.Model):
	datetime_start = models.DateTimeField()
	message_text = models.TextField()
	datetime_end = models.DateTimeField()
	# charfield с тегами через запятую  e.g. 'тест, важно, 123' или 1 тег
	filter_tag = models.CharField(max_length=255,  null=True, blank=True)
	# charfield с кодами через запятую  e.g. '901, 977, 921' или 1 код
	filter_op_codes = models.CharField(max_length=400,  null=True, blank=True)


class Messagetosend(models.Model):
	datetime_sent = models.DateTimeField(default=datetime.now)
	is_sent = models.BooleanField(default=False)
	context_part = models.ForeignKey(Mailinglist, null=True, blank=True, on_delete=models.SET_NULL)
	sending_to = models.ForeignKey(Client, null=True, blank=True, on_delete=models.SET_NULL)
