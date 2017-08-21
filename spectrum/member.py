# -*- coding: utf-8 -*-
from .object import Object
from .presence import Presence


class Member(Object):
    """Represents a Spectrum Member Object

    Supported Operations:

    +-----------+-----------------------------------------+
    | Operation |              Description                |
    +===========+=========================================+
    | x == y    | Checks if two members' are equal.       |
    +-----------+-----------------------------------------+
    | x != y    | Checks if two members' are not equal.   |
    +-----------+-----------------------------------------+
    | str(x)    | Returns the member's name.              |
    +-----------+-----------------------------------------+

    id : int
        The ID of the Member
    name : str
        The name chosen to be displayed publicly everywhere by the member
    handle : str
        The unique identifying name that the member chose
    avatar : str
        URL to the member's avatar
    presence : :class:`Presence`
        The presence of the member.
    roles : NotImplemented
        The roles held by the member. TODO
    """

    __slots__ = [
                'id', 'name', 'handle', 'avatar', 'presence', 'roles',
    ]

    def __init__(self, **kwargs):
        super(Member, self).__init__(kwargs.pop('id'))

        self.name = kwargs.pop('displayname')
        self.handle = kwargs.pop('nickname')
        self.avatar = kwargs.pop('avatar')

        # allows the presence to be passed from the cache if it already has it
        if isinstance(kwargs['presence'], Presence):
            self.presence = kwargs.pop('presence')
        else:
            self.presence = Presence(**kwargs.pop('presence'))

        self.roles = NotImplemented

    def __str__(self):
        return self.name
