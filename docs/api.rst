.. currentmodule:: spectrum

API Reference
===============

The following section outlines the API of spectrum.py.

Data Classes
--------------

.. warning::

    Nearly all data classes here have ``__slots__`` defined which means that it is
    impossible to have dynamic attributes to the data classes. The only exception
    to this rule is :class:`Object` which was designed with dynamic attributes in
    mind.

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
