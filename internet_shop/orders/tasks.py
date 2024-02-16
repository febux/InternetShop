from time import sleep
from django.core.mail import send_mail
from celery import shared_task

from orders.models import Order

from internet_shop import settings


@shared_task()
def send_order_email_task(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order {order.id}'
    message = f'{order.id}'
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[order.email],
    )
