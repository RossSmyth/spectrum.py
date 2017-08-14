# -*- coding: utf-8 -*-
from .object import Object

class Community(Object):
    """Represents a Spectrum Community
    
    Supported Operations:
    
    +-----------+--------------------------------------------+
    | Operation |                Description                 |
    +===========+============================================+
    | x == y    | Checks if two communities' are equal.      |
    +-----------+--------------------------------------------+
    | x != y    | Checks if two communities' are not equal.  |
    +-----------+--------------------------------------------+
    | str(x)    | Returns the communities' name.            |
    +-----------+--------------------------------------------+
    
    Attributes
    ----------
    id : int
        The ID of the community
    type : str
        The type of community. It can either be public or private.
        As far as I can tell, Public are CIG managed communities
        (not sure if evocati or subscriber communites are since I am not one)
        and private are orginizations.
    slug : str
        The shorthand abbreviation of the community
    name : str
        The name of the community
    avatar : str
        This is a URL for the avatar of the community
    banner : str
        This is a URL for the banner of the community
    lobbies : list
        A list of :class:`Lobby` that the community has. NOT IMPLEMENTED
    roles : list
        A list of the :class:`Role` that the community has. NOT IMPLEMENTED
    """
    
    __slots__ = [
                'id', 'type', 'slug', 'name', 'avatar', 'banner', 'lobbies',
                'roles'
                ]
                
    def __init__(self, **kwargs):
        super(Community, self).__init__(kwargs.pop('id'))
        
        self.type = kwargs.pop('type')
        self.slug = kwargs.pop('slug')
        self.name = kwargs.pop('name')
        self.avatar = kwargs.pop('avatar')
        self.banner = kwargs.pop('banner')
        
        self.lobbies = ['TODO'] #TODO
        
        self.roles = ['TODO'] #TODO
        
    def __str__(self):
        return self.name