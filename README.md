#Database of the Minor Planet Center

Dealing with the more than ~700,000 minor bodies of the Solar System
could be challenging.  The *Minor Planeet Center* (MPC) publishes regularly
updates of the database in different formats (see
http://www.minorplanetcenter.net/data).  

An efficient way to deal with this information is having it stored as
a MySQL database.  This is precisely the purpose of this simple
package.

We provide here an update version of the MPC database in a format that
can be manipulated in a MySQL server.  Once the MPC database is
updated, we provide updated versions of the database that can be
download and used in your server.

Getting the database
====================

To get the database just clone this repository:

   $ git clone http://github.com/seap-udea/MPCDatabase.git

The full-size of the MySQL dumped database is ~50 MB.

In order to manipulate the database you will need to install MySQL
server:

   $ sudo apt-get install mysql-server

For those manipulating the database with PHP or python we recommend to
install php5-mysql and python-mysqldb:

   $ sudo apt-get install php5-mysql python-mysqldb

Please keep the root password in a safe place you will need it oftenly.

Installing the database
=======================

Once cloned you should unpack and install the database.  

   $ make restore

This will create and populate the database "MinorBodies" in you MySQL
server.  You may want to create a special user for MySQL queries and
modifying the database.  The *user.sql* file contains the required
SQL commands to doing so.

   $ mysql -u root -p < user.sql


