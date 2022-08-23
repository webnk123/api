from .models import Mailinglist, Client,Messagetosend
import os
import datetime

import asyncio
import aiohttp
from asgiref.sync import sync_to_async


# runs every 60 seconds
# check if any mailing list is ready to be sent
# creates messages 
def create_messages():
	mailing_lists = list(Mailinglist.objects.filter(
		datetime_start__lte=datetime.datetime.now(), 
		datetime_end__gte=datetime.datetime.now())
	)

	for mailing_list in mailing_lists:
		clients_eligible_for_mailing = Client.objects.none()
		Clients = Client.objects.all()

		tags = filter_logic(mailing_list.filter_tag)
		op_codes = filter_logic(mailing_list.filter_op_codes)

		for x in tags:
			tagged = Client.objects.filter(tag=x)
			clients_eligible_for_mailing = clients_eligible_for_mailing | tagged
		for x in op_codes:
			tagged = Client.objects.filter(operator_code=x)
			clients_eligible_for_mailing = clients_eligible_for_mailing | tagged

		for i in clients_eligible_for_mailing:
			if Messagetosend.objects.filter(sending_to__id=i.id, context_part__id=mailing_list.id).exists():
				pass
			else:
				obj = Messagetosend()
				obj.datetime_sent = datetime.datetime.now()
				obj.is_sent = False
				obj.context_part = Mailinglist.objects.get(id = mailing_list.id)
				obj.sending_to = Client.objects.get(id = i.id)
				obj.start_sending = str(mailing_list.datetime_start).replace("T", " ") 
				obj.stop_sending = str(mailing_list.datetime_end).replace("T", " ")
				obj.save()		
				
	return clients_eligible_for_mailing



# parse tags and op_codes to return list
def filter_logic(stringtoparse):
	filterlist = []
	try:
		filterlist = stringtoparse.split(',')
		return filterlist
	except:
		return [stringtoparse]


@sync_to_async
def lookup_text(item):
	return str(item.context_part.message_text)


@sync_to_async
def lookup_phone(item):
	return str(item.sending_to.phone_number)


# update message "is_sent" field to true if resp code == 200
@sync_to_async
def update_messages(result):
	for i in result:
		if str(i[0]) == "200":
			item = Messagetosend.objects.get(pk=i[1])
			item.is_sent = True
			item.save()


async def fetch(client, item):
	url = "https://probe.fbrq.cloud/v1/send/" + str(item.id) 
	text = await lookup_text(item)
	phone = await lookup_phone(item)
	async with client.post(url=url, json={"id": int(item.id), "phone":int(phone), "text":str(text)}) as resp:
		html = await resp.text()
	return resp.status, item.id


async def main(messagelist):
	token =os.environ['TOKEN']
	header = {'Authorization': str(token)  }
	async with aiohttp.ClientSession(headers=header) as client:
		result = await asyncio.gather(*[
			asyncio.ensure_future(fetch(client, item))
			for item in messagelist
		])
		await update_messages(result)


# runs every 60 seconds
# gets all messages that can be sent
# sends via aiohttp

def send_messages():
	messagelist = list(Messagetosend.objects.filter(
		is_sent=False, 
		context_part__datetime_start__lte=datetime.datetime.now(), 
		context_part__datetime_end__gte=datetime.datetime.now())
	)


	loop = asyncio.new_event_loop()
	asyncio.set_event_loop(loop)
	loop.run_until_complete(main(messagelist))


