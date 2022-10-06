The ``models`` module
======================

Using ``Base``
-------------------

First import ``Base`` from the ``models/base`` module:

    >>> from models.base import Base

Now we use it:

check instantiation
	>>> merino = Base()
	>>> type(merino)
	<class 'models.base.Base'>

chech id auto encrement without give when a new instance is created
	>>> print(merino.id)
	1

chech id when a new instance is created
	>>> abel = Base(4)
	>>> print(abel.id)
	4
