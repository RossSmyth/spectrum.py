# -*- coding: utf-8 -*-


class Style_range:
    """Represents a Spectrum inlineStyleRange object

    Supported Operations:

    +-----------+-----------------------------------------+
    | Operation |              Description                |
    +===========+=========================================+
    | str(x)    | Returns the style_range's style.        |
    +-----------+-----------------------------------------+

    style : str
        The style that this style_range represents
    offset : int
        The offset of the style represented by the style_range from the
        beginning of the block
    length : int
        The length of the style represented by the style_range starting from the
        offset
    """

    __slots__ = [
                'style', 'offset', 'length',
    ]

    def __init__(self, style = None, offset = None, length = None):
        self.style = style
        self.offset = offset
        self.length = length

    def __str__(self):
        return self.style
