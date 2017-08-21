# -*- coding: utf-8 -*-


class Emoji:
    """Represents a Spectrum Emoji object

    Supported Operations:

    +-----------+-----------------------------------------+
    | Operation |              Description                |
    +===========+=========================================+
    | str(x)    | Returns the emoji's name.               |
    +-----------+-----------------------------------------+

    mutability : str
        Displays the mutability of the emoji. I do not know what this means in
        context, or when they are ever mutable. I have an open prize of 3 free
        original tapirs to anyone who can solve this.
    emoji : str
        Displays the name in the form :<name>: just taken from the raw JSON. I
        do not know if I will ever do able to code and decode from Unicode.
        There is a large block of Javascript in the Javascript that runs
        Spectrum that converts between str and an object, but I do not think I
        can convert between Unicode and str.
    offset : int
        The offset of where the emoji resides within the block.
    length : int
        The length of string that the emoji takes up from the offset in the raw
        block content.
    """

    __slots__ = [
                'mutability', 'emoji', 'offset', 'length'
                ]

    def __init__(self, **kwargs):
        self.mutability = kwargs.pop('mutability')
        self.emoji = kwargs.pop('data')
        self.offset = kwargs.pop('offset')
        self.length = kwargs.pop('length')

    def __str__(self):
        return self.emoji
