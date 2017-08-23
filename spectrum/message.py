# -*- coding: utf-8 -*-
from .object import Object
from .member import Member
from datetime import datetime
from .content import Content

class Message(Object):
    """Represents a Spectrum message object
    
    Supported Operations:
    
    +-----------+-----------------------------------------+
    | Operation |              Description                |
    +===========+=========================================+
    | x == y    | Checks if two messages are equal.       |
    +-----------+-----------------------------------------+
    | x != y    | Checks if two messages are not equal.   |
    +-----------+-----------------------------------------+
    | str(x)    | Returns the message's content. TODO     |
    +-----------+-----------------------------------------+

    id : int
        The ID of the Message
    time_created : ``datetime.datetime``
        The time that the message was created at
    time_modified : ``datetime.datetime``
        The time that the message was modified. NOTE: May be the same as the
        time that it was created. This just means it has not been modified. 
        Maybe changed in the future.
    lobby : :class:`Lobby`
        The lobby that the message was sent in. I know the general plan of how
        to execute this, but since a lobby object isn't sent with the message
        (which makes sense) I will have to pull it from the cache when the
        message is sent. I have it in my head of how it will work. # TODO
    author : :class:`Member`
        The author of the message. While this is a Member object, it is called
        author because it make more sense in context.
    content : :class:`Content`
        The content object in the message.
    media_id : str
        This is in the format of embed:<embed ID here>. It shows the embed ID
        if the message has an embed. Can be ``None`` if there are no embeds
    highlight_role : int or NotImplemented
        The role that the member used for that message. It may return an int if
        the role was not in the clients cache, or it may return a :class:`Role`
        object if it was in the clients cache.
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

        self.lobby = kwargs.pop('lobby')

        # This checks to see if networking found the author object in the cache
        if isinstance(kwargs['member'], Member):
            self.author = kwargs.pop('member')
        else:
            self.author = Member(**kwargs.pop('member'))

        self.content = Content(**kwargs.pop('content_state'))
        self.media_id = kwargs.pop('media_id')

        # checks if the role object was passed from the cache
        if isinstance(kwargs['highlight_role_id'], NotImplemented):
            self.highlight_role = kwargs.pop('highlight_role_id')
        else:
            self.highlight_role = int(kwargs.pop('highlight_role_id'))

        self.reactions = NotImplemented

    def __str__(self):
        return self.content.raw_content
