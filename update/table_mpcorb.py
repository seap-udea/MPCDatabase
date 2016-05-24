#!/usr/bin/env python
import json,gzip,re
import MySQLdb as mdb
from commands import getoutput as System

#############################################################
#CONNECT TO DATABASE
#############################################################
DATABASE="MinorBodies"
USER="minorbodies"
PASSWORD="347940"
con=mdb.connect("localhost",USER,PASSWORD,DATABASE)

#############################################################
#READ DATA
#############################################################
out=System("ls -m parts/*.json")
listf=out.split(",")
table=dict()
for jfile in listf:
    jfile=jfile.strip()
    print "Checking bodies in %s..."%jfile
    bodies=json.load(open(jfile))
    for body in bodies:
        for key in body.keys():
            if type(body[key]) is unicode:
                typeof="varchar(255)"
            elif type(body[key]) is list:
                typeof="varchar(100)"
            elif type(body[key]) is int:
                typeof="integer"
            elif type(body[key]) is float:
                typeof="real"
            else:
                typeof="varchar(255)"
            table[key]=typeof

f=open("database.sql","w")
f.write("use MinorBodies;\ncreate table Bodies (\n")
for key in table.keys():
    typeof=table[key]
    f.write("\t%s %s,\n"%(key,typeof))
f.write("\tprimary key (Principal_desig)\n")
f.write(");\n")
f.close()
