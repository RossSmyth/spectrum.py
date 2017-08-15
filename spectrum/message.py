# -*- coding: utf-8 -*-
from .object import Object
from datetime import datetime


class Message(Object):
    """Represents a Spectrum message
    
    Supported Operations:
    
    +-----------+-----------------------------------------+
    | Operation |              Description                |
    +===========+=========================================+
    | x == y    | Checks if two messages' are equal.      |
    +-----------+-----------------------------------------+
    | x != y    | Checks if two messages' are not equal.  |
    +-----------+-----------------------------------------+
    | str(x)    | Returns the message's content. TODO     |
    +-----------+-----------------------------------------+

    id : int
        The ID of the Message
    time_created : datetime.datetime.utcfromtimestamp
        The time that the message was created at
    time_modified : datetime.datetime.utcfromtimestamp
        The time that the message was modified. NOTE: May be the same as the
        time that it was created. This just means it has not been modified. 
        Maybe changed in the future.
    lobby : :class:`Lobby`
        The lobby that the message was sent in. I know the general plan of how
        to execute this, but since a lobby object isn't sent with the message
        (which makes sense) I will have to pull it from the cache when the
        message is sent. I have it in my head of how it will work. # TODO
    author : NotImplemented
        The author of the message. The API calls it "member." TODO
    content : NotImplemented
        The content of the message. Actually complicated. TODO
    media_id : NotImplemented
        I do not know what this is, but it is in the API. TODO
    highlight_role_id : NotImplemented
        Again, do not know what this is, but it is in the API. TODO
    reactions : NotImplemented
        The reactions to the message. TODO
    """

    __slots__ = [
                'id', 'time_created', 'time_modified', 'lobby', 'author',
                 'content', 'media_id', 'highlight_role_id', 'reactions',
                ]

    def __init__(self, **kwargs):
        super(Message, self).__init__(kwargs.pop('id'))

        self.time_created = datetime.utcfromtimestamp(
            kwargs.pop('time_created'))
        self.time_modified = datetime.utcfromtimestamp(
            kwargs.pop('time_modified'))

        self.lobby = kwargs.pop('lobby')  # TODO
        self.author = NotImplemented
        self.content = NotImplemented
        self.media_id = NotImplemented
        self.highlight_role_id = NotImplemented
        self.reactions = NotImplemented

    def __str__(self):
        return self.content  # TODO
