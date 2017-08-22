.. currentmodule:: spectrum

API Reference
===============

The following section outlines the API of spectrum.py.

Data Classes
--------------

.. warning::

    Most of the objects have __slots__ defined. This allows the API to save
    space in RAM, but it makes it so that it is impossible to have dynamic
    attributes to the data classes. I am sorry. There is one object,
    :class:`Object`, the does not have __slots__ defined. This is because it is
    made specifically so that dynamic attributes can be applied.

    More information about ``__slots__`` can be found
    `in the official python documentation <https://docs.python.org/3/reference/datamodel.html#slots>`_.

Object
~~~~~~~

.. autoclass:: Object
    :members:

Message
~~~~~~~~

.. autoclass:: Message
    :members:

Community
~~~~~~~~~~
.. autoclass:: Community
    :members:

Lobby
~~~~~~
.. autoclass:: Lobby
    :members:

Member
~~~~~~~
.. autoclass:: Member
    :members:

Presence
~~~~~~~~~
.. autoclass:: Presence
    :members:

Content
~~~~~~~~
.. autoclass:: Content
    :members:

Emoji
~~~~~~
.. autoclass:: Emoji
    :members:

Link
~~~~~
.. autoclass:: Link
    :members:

Mention
~~~~~~~~
.. autoclass:: Mention
    :members:

Block
~~~~~~
.. autoclass:: Block
    :members:
