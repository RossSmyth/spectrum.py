# -*- coding: utf-8 -*-
from .object import Object


class Lobby(Object):
    """Represents a Spectrum lobby object

    Supported Operations:

    +-----------+--------------------------------------------+
    | Operation |                Description                 |
    +===========+============================================+
    | x == y    | Checks if two lobbies' are equal.          |
    +-----------+--------------------------------------------+
    | x != y    | Checks if two lobbies' are not equal.      |
    +-----------+--------------------------------------------+
    | str(x)    | Returns the lobbies name.                  |
    +-----------+--------------------------------------------+

    id : int
        The ID of the lobby
    name : str
        The name of the lobby
    description : str
        The description of the lobby
    color : str
        The color of the lobby in hex
        (May make a color object in the future) #TODO
    online_members_count : int
        The number of members online
    key : str
        The API subscription key used to connect to the lobby
        (May make a key object in the future) #TODO
    permissions : NotImplemented
        Not sure if this is the special permission that the client has in this
        lobby, or something else. #TODO
    community : :class:`Community`
        The community that this lobby is a part of
    """

    __slots__ = [
                'id', 'type', 'name', 'description', 'color',
                'online_members_count', 'key', 'permissions', 'community'
    ]

    def __init__(self, **kwargs):
        super(Lobby, self).__init__(kwargs.pop('id'))

        self.type = kwargs.pop('type')
        self.name = kwargs.pop('name')
        self.description = kwargs.pop('description')
        self.color = kwargs.pop('color')
        self.online_members_count = kwargs.pop('online_member_count')
        self.key = kwargs.pop('subscription_key')
        self.community = kwargs.pop('community')

        self.permissions = [NotImplemented]  # TODO

    def __str__(self):
        return self.name
