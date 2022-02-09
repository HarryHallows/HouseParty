from django.db import models

import string
import random


def generate_unique_code():  # Generates unique Code for a room

    length = 6

    while True:

        # Creates a random assortment of ascii characters in uppercase within the size of length (6)
        code = ''.join(random.choices(string.ascii_uppercase, k=length))

        # If there's no rooms with the current generated code within the database then break from while loop
        if Room.objects.filter(code=code).count() == 0:
            break

    # Once Unique Code is generated return code value
    return code

# Create your models here.


class Room(models.Model):

    code = models.CharField(max_length=8, default="",
                            unique=True)  # Lobby Passcode

    host = models.CharField(max_length=50, unique=True)  # Host Name

    # Checks if the guests are allowed to pause songs
    guest_can_pause = models.BooleanField(null=False, default=False)

    # How many votes required to skip the song
    votes_to_skip = models.IntegerField(null=False, default=1)

    # On room creation it will automatically log the time
    created_at = models.DateTimeField(auto_now_add=True)
