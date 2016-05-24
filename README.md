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

<option value="Ab">SPK-ID</option>
<option value="Ad">prim. desig.</option>
<option value="Ae">IAU name</option>
<option value="Af">prefix</option>
<option value="Ai">H (mag)</option>
<option value="Aj">G</option>
<option value="Ak">M1 (mag)</option>
<option value="Al">M2 (mag)</option>
<option value="Am">K1</option>
<option value="An">K2</option>
<option value="Ao">PC</option>
<option value="Ap">diameter (km)</option>
<option value="Aq">extent (km)</option>
<option value="Ar">albedo</option>
<option value="As">rot_per (h)</option>
<option value="At">GM (km^3/s^2)</option>
<option value="Au">B-V (mag)</option>
<option value="Av">U-B (mag)</option>
<option value="Aw">I-R (mag)</option>
<option value="Ax">spec. type (SMASSII)</option>
<option value="Ay">spec. type (Tholen)</option>
<option value="Az">H-sigma (mag)</option>
<option value="Ba">diameter-sigma (km)</option>
</select></td> <td nowrap><label for="2"></label><select name="OBJ_op" tabindex="2"  id="2">
<option value="0">( operator )</option>
<option value="&lt;">&lt;</option>
<option value="&lt;=">&lt;=</option>
<option value="=">=</option>
<option value="&gt;=">&gt;=</option>
<option value="&gt;">&gt;</option>
<option value="range">range</option>
<option value="!=">!=</option>
<option value="REGEXP">REGEXP</option>
<option value="defined">defined</option>
<option value="not defined">not defined</option>
</select></td> <td nowrap><input type="text" name="OBJ_value"  1 24="-default" 8="-maxlength" ="-override" alt="0" /></td> <td nowrap><input type="submit" name="add_OBJ" value="Add =&gt;" /></td></tr></table>
</td></tr> <tr><td align="right"><table border="0" cellpadding="4" cellspacing="0"><tr valign="middle"><td nowrap><label for="5"></label><select name="ORB_field" tabindex="5"  id="5">
<option selected="selected" value="0">( select orbital parameter )</option>
<option value="Bg">e</option>
<option value="Bh">a (AU)</option>
<option value="Bi">q (AU)</option>
<option value="Bj">i (deg)</option>
<option value="Bk">node (deg)</option>
<option value="Bl">peri (deg)</option>
<option value="Bm">M (deg)</option>
<option value="Bn">Q (AU)</option>
<option value="Bo">n (deg/d)</option>
<option value="Bp">tp (JED)</option>
<option value="Bq">tp (ET)</option>
<option value="Br">period (d)</option>
<option value="Bs">period (years)</option>
<option value="Bt">Earth MOID (AU)</option>
<option value="Bu">Earth MOID (LD)</option>
<option value="Bv">Jupiter MOID (AU)</option>
<option value="Bw">T-Jupiter</option>
<option value="Bx">e-sigma</option>
<option value="By">a-sigma (AU)</option>
<option value="Bz">q-sigma (AU)</option>
<option value="Ca">i-sigma (deg)</option>
<option value="Cb">node-sigma (deg)</option>
<option value="Cc">peri-sigma (deg)</option>
<option value="Cd">M-sigma (deg)</option>
<option value="Ce">Q (1-sigma) (AU)</option>
<option value="Cf">n (1-sigma) (deg/d)</option>
<option value="Cg">tp-sigma (d)</option>
<option value="Ch">period-sigma (d)</option>
<option value="Ck">data-arc span (d)</option>
<option value="Co"># obs. used (del.)</option>
<option value="Cp"># obs. used (dop.)</option>
<option value="Cq">condition code</option>
<option value="Cs">two-body model (T/F)</option>
<option value="Ct">A1</option>
<option value="Cu">A2</option>
<option value="Cv">A3</option>
<option value="Cw">DT (d)</option>
</select></td> <td nowrap><label for="6"></label><select name="ORB_op" tabindex="6"  id="6">
<option value="0">( operator )</option>
<option value="&lt;">&lt;</option>
<option value="&lt;=">&lt;=</option>
<option value="=">=</option>
<option value="&gt;=">&gt;=</option>
<option value="&gt;">&gt;</option>
<option value="range">range</option>
<option value="!=">!=</option>
<option value="REGEXP">REGEXP</option>
<option value="defined">defined</option>
<option value="not defined">not defined</option>
</select></td> <td nowrap><input type="text" name="ORB_value"  1 24="-default" 8="-maxlength" ="-override" alt="0" /></td> <td nowrap><input type="submit" name="add_ORB" value="Add =&gt;" /></td></tr></table>
</td></tr></table>
</td> <td align="left" width="50%"><em>no constraints</em>
</td></tr></table>
<br>
<table bgcolor="#006600" border="0" cellpadding="2" cellspacing="0"><tr><td>&nbsp;</td> <td align="left" nowrap><font class="section_text">Output Fields:</font></td> <td width="100%">&nbsp;</td> <td align="right" nowrap><b><a href="/?help_sbdb_query#fields" target="_blank"><font color="#FFFFFF">help</font></a></b></td> <td>&nbsp;&nbsp;&nbsp;</td></tr></table>
<table bgcolor="#FFFFFF" border="1" cellpadding="4" cellspacing="0" width="100%"><tr><td align="left"><table bgcolor="#FFFFCC" border="0" cellpadding="2" cellspacing="0"><tr valign="top"><td align="right">&nbsp;<b>Step 2:</b></td> <td align="left">select desired output fields from the lists below or pick from defined sets<br>(you can add fields one at a time or in groups)</td> <td align="left">&nbsp;</td></tr>
</table>
<table border="0" cellpadding="4" cellspacing="0"><tr valign="top"><td align="left" nowrap><b><label for="9">Object Fields:</label></b><br>
<select name="OBJ_field_set" tabindex="9"  size="10" multiple="multiple" id="9">
<option value="Aa">object internal database ID</option>
<option value="Ab">object primary SPK-ID</option>
<option value="Ac">object full name/designation</option>
<option value="Ad">object primary designation</option>
<option value="Ae">object IAU name</option>
<option value="Af">comet designation prefix</option>
<option value="Ag">Near-Earth Object (NEO) flag (Y/N)</option>
<option value="Ah">Potentially Hazardous Asteroid (PHA) flag (Y/N)</option>
<option value="Ai">[ H ] absolute magnitude parameter (mag)</option>
<option value="Aj">[ G ] magnitude slope parameter (default is 0.15)</option>
<option value="Ak">[ M1 ] comet total magnitude parameter (mag)</option>
<option value="Al">[ M2 ] comet nuclear magnitude parameter (mag)</option>
<option value="Am">[ K1 ] comet total magnitude slope parameter</option>
<option value="An">[ K2 ] comet nuclear magnitude slope parameter</option>
<option value="Ao">[ PC ] comet nuclear magnitude law - phase coefficient</option>
<option value="Ap">object diameter (from equivalent sphere) (km)</option>
<option value="Aq">object bi/tri-axial ellipsoid dimensions (km)</option>
<option value="Ar">geometric albedo</option>
<option value="As">rotation period (h)</option>
<option value="At">[ GM ] mass expressed as product mass and grav. const. G (km^3/s^2)</option>
<option value="Au">color index B-V (mag)</option>
<option value="Av">color index U-B (mag)</option>
<option value="Aw">color index I-R (mag)</option>
<option value="Ax">spectral taxonomic type (SMASSII)</option>
<option value="Ay">spectral taxonomic type (Tholen)</option>
<option value="Az">1-sigma uncertainty in abs. mag. param. H (mag)</option>
<option value="Ba">1-sigma uncertainty in object diameter (km)</option>
</select>
</td> <td align="left" nowrap><b><label for="10">Orbital and Model Parameter Fields:</label></b><br>
<select name="ORB_field_set" tabindex="10"  size="10" multiple="multiple" id="10">
<option value="Bb">orbit solution ID</option>
<option value="Bc">epoch of osculation (JED)</option>
<option value="Bd">epoch of osculation (MJD)</option>
<option value="Be">epoch of osculation (ET)</option>
<option value="Bf">equinox of reference frame</option>
<option value="Bg">[ e ] eccentricity</option>
<option value="Bh">[ a ] semi-major axis (AU)</option>
<option value="Bi">[ q ] perihelion distance (AU)</option>
<option value="Bj">[ i ] inclination (deg)</option>
<option value="Bk">longitude of the ascending node (deg)</option>
<option value="Bl">argument of perihelion (deg)</option>
<option value="Bm">[ M ] mean anomaly (deg)</option>
<option value="Bn">[ Q ] aphelion distance (AU)</option>
<option value="Bo">[ n ] mean motion (deg/d)</option>
<option value="Bp">time of perihelion passage (JED)</option>
<option value="Bq">time of perihelion passage (ET)</option>
<option value="Br">orbital period (d)</option>
<option value="Bs">orbital period (years)</option>
<option value="Bt">Earth Minimum Orbit Intersection Distance (AU)</option>
<option value="Bu">Earth Minimum Orbit Intersection Distance (LD)</option>
<option value="Bv">Jupiter Minimum Orbit Intersection Distance (AU)</option>
<option value="Bw">Jupiter Tisserand Invariant</option>
<option value="Bx">eccentricity (1-sigma uncertainty)</option>
<option value="By">semi-major axis (1-sigma uncertainty) (AU)</option>
<option value="Bz">perihelion distance (1-sigma uncertainty) (AU)</option>
<option value="Ca">inclination (1-sigma uncertainty) (deg)</option>
<option value="Cb">long. of the asc. node (1-sigma uncertainty) (deg)</option>
<option value="Cc">argument of perihelion (1-sigma uncertainty) (deg)</option>
<option value="Cd">mean anomaly (1-sigma uncertainty) (deg)</option>
<option value="Ce">aphelion distance (1-sigma uncertainty) (AU)</option>
<option value="Cf">mean motion (deg/d)</option>
<option value="Cg">time of peri. passage (1-sigma uncertainty) (d)</option>
<option value="Ch">orbital period (1-sigma uncertainty) (d)</option>
<option value="Ci">orbit classification</option>
<option value="Cj">name of person (or institution) who computed the orbit</option>
<option value="Ck">number of days spanned by the data-arc (d)</option>
<option value="Cl">date of first observation used in the orbit fit (UT)</option>
<option value="Cm">date of last observation used in the orbit fit (UT)</option>
<option value="Cn">number of observations (all types) used in fit</option>
<option value="Co">number of delay-radar observations used in fit</option>
<option value="Cp">number of Doppler-radar observations used in fit</option>
<option value="Cq">orbit condition code (MPC &#39;U&#39; parameter)</option>
<option value="Cr">normalized RMS of orbit fit (arcsec)</option>
<option value="Cs">2-body dynamics used flag (T/F)</option>
<option value="Ct">[ A1 ] non-grav. radial parameter</option>
<option value="Cu">[ A2 ] non-grav. transverse parameter</option>
<option value="Cv">[ A3 ] non-grav. normal parameter</option>
<option value="Cw">[ DT ] non-grav. peri.-maximum offset (d)</option>

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


