# -*- coding: utf-8 -*-
from .object import Object
from .style_range import Style_range
from .entities import Emoji, Mention, Link


class Block(Object):
    """Represents a Spectrum block object
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
                self.entities.append(link(**mapped_entity, **entity))
