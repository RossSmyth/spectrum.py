# -*- coding: utf-8 -*-
from .object import Object
from .style_range import Style_range
from .entities import Emoji, Mention, Link


class Block(Object):
    """Represents a Spectrum block object

    Supported Operations:

    +-----------+--------------------------------------+
    | Operation |             Description              |
    +===========+======================================+
    | x == y    | Checks if two blocks are equal.      |
    +-----------+--------------------------------------+
    | x != y    | Checks if two blocks are not equal.  |
    +-----------+--------------------------------------+
    | str(x)    | Returns the block's text.            |
    +-----------+--------------------------------------+

    This object represents each individual line in a Spectrum message. For
    example if you press Shift+Enter to create a new line, this would be a new
    block in the message. Also each code block wrapper in ``` would be its own
    block.

    id : str
        The ID of the block.

        .. warning::

            Most of the ID attributes for objects in Spectrum are an ``int``,
            but this ID is a ``str``. I do not know why

    text : str
        The raw text that makes up the block
    type : str
        Represents the type of text in the whole block
        Can be one of the following:
            - unstyled
            - code-block
            - ???
    depth : int
        I do not know what this is. But it is here
    style_ranges :
        A ``list`` of :class:`Style_range` that are in the block
    entities :
        A ``list`` of either :class:`Emoji`, :class:`Mention`, or :class:`Link`
        that are in the block's content.
    """

    __slots__ = [
                'id', 'text', 'type', 'depth', 'style_ranges', 'entities',
    ]

    def __init__(self, **kwargs):
        self.id = kwargs.pop('key')
        self.text = kwargs.pop('text')
        self.type = kwargs.pop('type')
        self.depth = kwargs.pop('depth')

        self.style_ranges = [Style_range(**style_range) for style_range in
                             kwargs.pop('inlineStyleRanges')]

        self.entities = []

        _entity_ranges = kwargs.pop('entityRanges')
        self._get_entities(kwargs.pop('entity_map'), _entity_ranges)

    def _get_entities(self, entity_map, entity_ranges):
        if entity_ranges == [] or entity_map == []: return  # Check now

        for entity in entity_ranges:
            mapped_entity = entity_map[entity['key']]  # prevents messes later

            if mapped_entity['type'].lower() == 'emoji':
                self.entities.append(Emoji(**mapped_entity, **entity))

            elif mapped_entity['type'].lower() == 'mention':
                self.entities.append(Mention(**mapped_entity, **entity))

            elif mapped_entity['type'].lower() == 'link':
                self.entities.append(Link(**mapped_entity, **entity))

    def __str__(self):
        return self.text