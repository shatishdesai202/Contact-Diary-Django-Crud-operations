from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(user_logged_in, sender=User)
def login_ip(sender, request, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    request.session['ip'] = ip
    print(ip)
