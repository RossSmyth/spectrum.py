# -*- coding: utf-8 -*-
from .object import Object
from .lobby import Lobby


class Community(Object):
    """Represents a Spectrum Community object
    
    Supported Operations:
    
    +-----------+--------------------------------------------+
    | Operation |                Description                 |
    +===========+============================================+
    | x == y    | Checks if two communities are equal.       |
    +-----------+--------------------------------------------+
    | x != y    | Checks if two communities are not equal.   |
    +-----------+--------------------------------------------+
    | str(x)    | Returns the community's name.              |
    +-----------+--------------------------------------------+

    id : int
        The ID of the community
    type : str
        The type of community.
        Can be one of the following: (to my knowledge)
            - Public
            - Private
    slug : str
        The shorthand abbreviation of the community
    name : str
        The name of the community
    avatar : str
        This is a URL for the avatar of the community
    banner : str
        This is a URL for the banner of the community
    lobbies :
        An iterable :class:`Lobby` that the community has.
    roles : NotImplemented
        A list of the :class:`Role` that the community has. #TODO
    """

    __slots__ = [
                'id', 'type', 'slug', 'name', 'avatar', 'banner', '_lobbies',
                'roles'
    ]

    def __init__(self, **kwargs):
        super(Community, self).__init__(kwargs.pop('id'))

        self.type = kwargs.pop('type')
        self.slug = kwargs.pop('slug')
        self.name = kwargs.pop('name')
        self.avatar = kwargs.pop('avatar')
        self.banner = kwargs.pop('banner')

        self._lobbies = {}  # allows for easy lookup of lobbies by ID number
        _lobbies_json = kwargs.pop('lobbies')
        for l in _lobbies_json:
            lobby = Lobby(community=self, **l)
            self._lobbies[lobby.id] = lobby

        self.roles = [NotImplemented]  # TODO

    @property
    def lobbies(self):
        return self._lobbies.values()

    def __str__(self):
        return self.name
