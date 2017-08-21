# -*- coding: utf-8 -*-
from datetime import datetime


class Presence:
    """Represents a Spectrum Presence object

    Supported Operations:

    +-----------+--------------------------------------+
    | Operation |             Description              |
    +===========+======================================+
    | str(x)    | Returns the presence's status        |
    +-----------+--------------------------------------+

    status : str
         Returns the status of the member.
         Can be one of the following:
            - away
            - online
            - do_not_disturb
            - invisible

    info : str/None
        Returns a string of what the member is doing.
        If the member is playing Star Citizen it can be one of two things:
            - "Playing Star Citizen" if they are currently in game
            - "In Menus" if they have the game open, but are in in game

    since : ``datetime.datetime``
        Return a datetime object from when this member's presence has changed
    """

    __slots__ = [
                'status', 'info', 'since',
    ]

    def __init__(self, **kwargs):

        self.status = kwargs.pop('status')
        self.info = kwargs.pop('info')
        self.since = datetime.utcfromtimestamp(kwargs.pop('since'))

    def __str__(self):
        return self.status
