from django.db import connection
from django.db.backends.signals import connection_created
from django.core.signals import request_finished
from django.dispatch import receiver


@receiver(connection_created)
def connection_opened(sender, connection, **kwargs):
    print("Connection to database opened")


@receiver(request_finished)
def connection_closed(sender, **kwargs):
    connection.close()
    print("Connection to database closed")