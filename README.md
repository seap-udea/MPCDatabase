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

```
	$ git clone http://github.com/seap-udea/MPCDatabase.git
```

The full-size of the MySQL dumped database is ~50 MB.

In order to manipulate the database you will need to install MySQL
server:

```
	$ sudo apt-get install mysql-server
```

For those manipulating the database with PHP or python we recommend to
install php5-mysql and python-mysqldb:

```
	$ sudo apt-get install php5-mysql python-mysqldb
```

Please keep the root password in a safe place you will need it oftenly.

Installing the database
=======================

Once cloned you should unpack and install the database.  

```
        $ make restore
```

This will create and populate the database "MinorBodies" in you MySQL
server.  You may want to create a special user for MySQL queries and
modifying the database.  The *user.sql* file contains the required
SQL commands to doing so.

```
       $ mysql -u root -p < user.sql
```

Database fields
===============

The fields of the MPC Database are fully described in the Guide to the
[Extended Versions of MPC Data Files Based on the MPCORB
Format](http://minorplanetcenter.net/Extended_Files/Extended%20MPCORB%20Data%20Format%20Manual.pdf).
Here we provide a summary:

* **Name** (string): Name, if the asteroid has received one.

* **Number** (string): Number, if the asteroid has received one; this
  is the asteroid's permanent designation.

* **Principal_desig** (string): Principal provisional designation (if it
  exists) 

* **Other_desigs** (string): Other provisional designations (if they
  exist).

* **H** (float): Absolute magnitude, H

* **G** (float): Slope parameter, G

* **Epoch* * (float): Epoch of the orbit (Julian Date).

* **a** (float): Semimajor axis, a (AU).

* **e** (float): Orbital eccentricity, e.

* **i** (float): Inclination to the ecliptic, J2000.0 (degrees).

* **Node** (float): Longitude of the ascending node, ☊, J2000.0 (degrees).

* **Peri** (float): Argument of perihelion, ω, J2000.0 (degrees).

* **M** (float): Mean anomaly, M, at the epoch (degrees).

* **n** (float): Mean daily motion, n (degrees/day).

* **U** (string): Uncertainty parameter, U (integer with values 0–9; but
  refer to entry in Table 1 for other possible values)

* **Ref** (string): Reference

* **Num_obs** (integer): Number of observations.

* **Num_opps** (integer): Number of oppositions.

* **Arc_years** (string): Only present for multi-opposition orbits
  (year of first observation – year of last observation).

* **Arc_length** (integer): Only present for 1-opposition orbits
  (days).

* **rms** (float): r.m.s. residual (").

* **Perturbers** (string): Coarse indicator of perturbers used in
  orbit computation.

* **Perturbers_2** (string): Precise indicator of perturbers used in
  orbit computation.

* **Last_obs** (string): Date of last observation included in orbit
  solution (YYYY-MM-DD format)

* **Hex_flags** (string): 4-hexdigit flags (refer to entry in Table 1
  for explanation; in JSON format this information has been decoded
  and is supplied in individual keywords) Computer string Name of
  orbit computer (be it a person or machine).

* **orbit_type** (string): Possible values:

    • Atira
    • Aten
    • Apollo
    • Amor
    • Object with perihelion distance < 1.665 AU
    • Hungaria
    • MBA
    • Phocaea
    • Hilda
    • Jupiter Trojan
    • Distant Object
    • Unclassified

* **NEO_flag** (integer): Value = 1 if flag raised, otherwise keyword is absent.

* **One_km_NEO_flag** (integer): Value = 1 if flag raised, otherwise keyword is absent.

* **PHA_flag** (integer): Value = 1 if flag raised, otherwise keyword is absent.

* **One_opposition_object_flag** (integer): Value = 1 if flag raised,
    otherwise keyword is absent.

* **Critical_list_numbered_object_flag** (integer): Value = 1 if flag
    raised, otherwise keyword is absent.

* **Perihelion_dist** (float): Perihelion distance (AU).

* **Aphelion_dist** (float): Aphelion distance (AU).

* **Semilatus_rectum** (float): Semilatus rectum distance (AU).

* **Orbital_period** (float): Orbital period (years).

* **Synodic_period** (float): Synodic period (years).

NASA Small Bodies Database
==========================

In order to complement the MPC database we have also added to this
database the information contained in the [NASA Minor Bodies
Database](http://ssd.jpl.nasa.gov/sbdb_query.cgi).  This database is
somewhat complimentary since it also includes physical information
about the minorbodies (albedo, diameter, spectral class, etc.).

All this information is contained in the separate table
``MinorBodies`` (the MPC information is in the ``Bodies`` database).

The fields of this database are:

Physical:

* **id**: object internal database ID.
* **spkid**: object primary SPK-ID.
* **full_name**: object full name/designation.
* **pdes**: object primary designation.
* **name**: object IAU name.
* **prefix**: comet designation prefix.
* **neo**: Near-Earth Object (NEO) flag (Y/N).
* **pha**: Potentially Hazardous Asteroid (PHA) flag (Y/N).
* **H**: [ H ] absolute magnitude parameter (mag).
* **G**: [ G ] magnitude slope parameter (default is 0.15).
* **M1**: [ M1 ] comet total magnitude parameter (mag).
* **M2**: [ M2 ] comet nuclear magnitude parameter (mag).
* **K1**: [ K1 ] comet total magnitude slope parameter.
* **K2**: [ K2 ] comet nuclear magnitude slope parameter.
* **PC**: [ PC ] comet nuclear magnitude law - phase coefficient.
* **diameter**: object diameter (from equivalent sphere) (km).
* **extent**: object bi/tri-axial ellipsoid dimensions (km).
* **albedo**: geometric albedo.
* **rot_per**: rotation period (h).
* **GM**: [ GM ] mass expressed as product mass and grav. const. G (km^3/s^2).
* **BV**: color index B-V (mag).
* **UB**: color index U-B (mag).
* **IR**: color index I-R (mag).
* **spec_B**: spectral taxonomic type (SMASSII).
* **spec_T**: spectral taxonomic type (Tholen).
* **H_sigma**: 1-sigma uncertainty in abs. mag. param. H (mag).
* **diameter_sigma**: 1-sigma uncertainty in object diameter (km).

Orbital:

* **orbit_id**: orbit solution ID.
* **epoch**: epoch of osculation (JED).
* **epoch_mjd**: epoch of osculation (MJD).
* **epoch_cal**: epoch of osculation (ET).
* **equinox**: equinox of reference frame.
* **e**: [ e ] eccentricity.
* **a**: [ a ] semi-major axis (AU).
* **q**: [ q ] perihelion distance (AU).
* **i**: [ i ] inclination (deg).
* **om**: longitude of the ascending node (deg).
* **w**: argument of perihelion (deg).
* **ma**: [ M ] mean anomaly (deg).
* **ad**: [ Q ] aphelion distance (AU).
* **n**: [ n ] mean motion (deg/d).
* **tp**: time of perihelion passage (JED).
* **tp_cal**: time of perihelion passage (ET).
* **per**: orbital period (d).
* **per_y**: orbital period (years).
* **moid**: Earth Minimum Orbit Intersection Distance (AU).
* **moid_ld**: Earth Minimum Orbit Intersection Distance (LD).
* **moid_jup**: Jupiter Minimum Orbit Intersection Distance (AU).
* **t_jup**: Jupiter Tisserand Invariant.
* **sigma_e**: eccentricity (1-sigma uncertainty).
* **sigma_a**: semi-major axis (1-sigma uncertainty) (AU).
* **sigma_q**: perihelion distance (1-sigma uncertainty) (AU).
* **sigma_i**: inclination (1-sigma uncertainty) (deg).
* **sigma_om**: long. of the asc. node (1-sigma uncertainty) (deg).
* **sigma_w**: argument of perihelion (1-sigma uncertainty) (deg).
* **sigma_ma**: mean anomaly (1-sigma uncertainty) (deg).
* **sigma_ad**: aphelion distance (1-sigma uncertainty) (AU).
* **sigma_n**: mean motion (1-sigma uncertainty) (deg/d).
* **sigma_tp**: time of peri. passage (1-sigma uncertainty) (d).
* **sigma_per**: orbital period (1-sigma uncertainty) (d).
* **class**: orbit classification.
* **producer**: name of person (or institution) who computed the orbit.
* **data_arc**: number of days spanned by the data-arc (d).
* **first_obs**: date of first observation used in the orbit fit (UT).
* **last_obs**: date of last observation used in the orbit fit (UT).
* **n_obs_used**: number of observations (all types) used in fit.
* **n_del_obs_used**: number of delay-radar observations used in fit.
* **n_dop_obs_used**: number of Doppler-radar observations used in fit.
* **condition_code**: orbit condition code (MPC parameter).
* **rms**: normalized RMS of orbit fit (arcsec).
* **two_body**: 2-body dynamics used flag (T/F).
* **A1**: [ A1 ] non-grav. radial parameter.
* **A2**: [ A2 ] non-grav. transverse parameter.
* **A3**: [ A3 ] non-grav. normal parameter.
* **DT**: [ DT ] non-grav. peri.-maximum offset (d).

Working with the database
=========================

Once installed you may manipulate the database from different
languages (PHP, Pyhton, Perl, etc.).

Here is an example of the database manipulation using Python:

```python
import MySQLdb as mdb
DATABASE="MinorBodies"
USER="minorbodies"
PASSWORD="347940"
con=mdb.connect("localhost",USER,PASSWORD,DATABASE)
db=con.cursor()

db.execute("show columns from Bodies")
fields=db.fetchall()

db.execute("select * from Bodies where Name like '%zuluaga%'")
results=db.fetchone()

for i in xrange(len(results)):
    print fields[i][0],":",results[i]
```

You may also consider load a utility python package provided with the
repositiory, namely **mpcdb.py**.

```python
from mpcdb import *
results=mysqlSelect(condition="limit 100")
print results
```

Where ``mysqlSelect`` has the following syntax:

```
      mysqlSelect(selection="*",table="Bodies",condition="")
```

Examples:

* ``mysqlSelect()``: Select the first 100 the bodies in the
  database (it could be very slow).  This is useful if running the
  test under ipython.

* ``mysqlSelect(selection="max(a)")``: show the maximum value of the
  semimajor axis in the database.

*
  ``mysqlSelect(selection="Name,Principal_desig",condition="where NEO_flag<>0
  or PHA_flag<>0")``: return all NEOs and PHAs.

* ``mysqlSelect(selection="a",condition="sorted by a asc")``: return
  semimajor axes in ascending order.

Read only if you are a contributor
==================================

You may clone a working copy of the repository using:

```
git clone git@github.com:seap-udea/MPCDatabase
```

To update the MPC database download the [json gzipped file from the
MPC
website](http://minorplanetcenter.net/Extended_Files/mpcorb_extended.json.gz)
into the update directory of the MPCDatabase working directory.  

You need also to download the CSV file containing the NASA Minor
Bodies Database using [this on-line
form](http://ssd.jpl.nasa.gov/sbdb_query.cgi).  Be sure to select all
fields in the orbital and physical properties.

Once downloaded you must have two large files (~50 Mb and ~380 Mb
respectively): **mpcorb_extended.json.gz** and **results.csv**.  Both
files should be in the update directory.

Once there split the json file into smaller pieces (blocks, containing
500 objects each):

```
python read_mpcorb.py
```

There are approximately ~1400 blocks. Then save the properties of the
objects in the database:

```
python save_mpcorb.py
```

Now it's time for updating the NSBD.  Run the script:

```
python save_nsbd.py
```

There is a total of ~700,000 minor bodies, so you should be patient.

Once updated clean the directory:

```
make clean
```

and backup the database (go to the root directory of the MPCDatabase repository):

```
make backup
```

Upload the results to the repository:

```
make commit
```


