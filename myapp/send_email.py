from django.core.mail import send_mail
from .models import Mailinglist, Messagetosend




def send_email():
    template = ""

    Mailing = Mailinglist.objects.all()
    for i in Mailing:
        x = Messagetosend.objects.filter(context_part=i.id).count()
        y = Messagetosend.objects.filter(context_part=i.id, is_sent=True).count()
        z = Messagetosend.objects.filter(context_part=i.id, is_sent=False).count()
        
        template += "Отчет по рассылке№ " + str(i.id) + "\n" + "Всего сообщений:" + str(x) + "Отправленных: " + str(y) + " Не отправленных: " + str(z) + "\n"

    print(template)

# настроить ящик можно в settings.py
'''
    send_mail(
        'Статистика',
        template,
        'from@example.com',
        ['to@example.com'],
        fail_silently=True,
    )
'''
