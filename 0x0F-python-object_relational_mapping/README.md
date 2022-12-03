#0x0F. Python - Object-relational mapping
=============================================

##Background Context

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

##Resources
Read or watch:
-Object-relational mappers
-mysqlclient/MySQLdb documentation (please don’t pay attention to _mysql)
-MySQLdb tutorial
-SQLAlchemy tutorial
-SQLAlchemy
-mysqlclient/MySQLdb
-Introduction to SQLAlchemy
-Flask SQLAlchemy
-10 common stumbling blocks for SQLAlchemy newbies
-Python SQLAlchemy Cheatsheet
-SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)
-SQLAlchemy Tutorial

##More Info
Install MySQLdb module version 2.0.x

For installing MySQLdb, you need to have MySQL installed: How to install MySQL 8.0 in Ubuntu 20.04

$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)

Install SQLAlchemy module version 1.4.x

$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'

Also, you can have this warning message:

/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  

You can ignore it.
