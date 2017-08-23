# -*- coding: utf-8 -*-
from .block import Block


class Content:
    """Represents a Spectrum content object

    Supported Operations:

    +-----------+-----------------------------------------+
    | Operation |              Description                |
    +===========+=========================================+
    | str(x)    | Returns the content's raw_content.      |
    +-----------+-----------------------------------------+

    lines : int
        The number of blocks that makes up the Content object
    blocks : list
        A ``list`` of :class:`Block` objects that makes up the Content object.
        Each block represents a line in the message.
    raw_content : str
        The raw content string of the message. Every block (line) ends with a
        ' \\\\n' before the next block (line) starts.
    """

    __slots__ = [
                'lines', 'blocks', 'raw_content', 'emojis', 'mentions'
    ]

    def __init__(self, **kwargs):

        self.lines = len(kwargs['blocks'])

        self.blocks = [Block(**_block) for _block in kwargs.pop('blocks')]

        self.raw_content = ' \n'.join(_block.text for _block in self.blocks)

    def __str__(self):
        return self.raw_content
