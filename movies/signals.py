from django.core.mail import send_mail
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Movie


@receiver(post_save, sender=Movie)
def my_handler(sender, instance, created, *args, **kwargs):
    if created:
        name = instance.name
        send_mail(
            subject='MyApp',
            message='Hi, New Movie {} has been created'.format(name),
            from_email='testestest382@mail.com',
            recipient_list=['reemsamir521999@gmail.com'],
            fail_silently=True)