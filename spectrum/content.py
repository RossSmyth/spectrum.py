# -*- coding: utf-8 -*-


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
    blocks : NotImplemented
        A ``list`` of :class:`Block` objects that makes up the Content object
    raw_content : NotImplemented
        The raw content data of the message without any emojis or mentions put
         in.
    emojis : NotImplemented
        A ``list`` of :class:`Emoji` objects that make up the Content object
    mentions : NotImplemented
        A ``list`` of :class:`Mention` objects that make up the Content object
    """

    def __init__(self, **kwargs):

        self.lines = len(kwargs['blocks'])

        self.blocks = [NotImplemented]  # TODO
        self.raw_content = NotImplemented
        self.emojis = [NotImplemented]
        self.mentions = [NotImplemented]

    def __str__(self):
        return self.raw_content
