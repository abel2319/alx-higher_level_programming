The ``models`` module
======================

Using ``Rectangle``
-------------------

First import ``Reactangle`` from the ``models/rectangle`` module:

    >>> from models.rectangle import Rectangle

Now we use it:

check normal instantiation
	>>> merino = Rectangle(10, 2, 0, 0, 12)
	>>> type(merino)
	<class 'models.rectangle.Rectangle'>

chech id auto encrement without give when a new instance is created
	>>> print(merino.id)
	12

chech instantiation with just 2 arguments
	>>> abel = Rectangle(10, 2)
	>>> print(abel.id)
	4

	>>> print(abel.width)
	10
	
	>>> print(abel.height)
	2

	>>> print(abel.x)
	0
	
	>>> print(abel.y)
	0
	
	>>> print(abel.id)
	1
