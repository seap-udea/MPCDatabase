#!/usr/bin/env python
import json,gzip,re
import MySQLdb as mdb
import sys
from commands import getoutput as System

def replaceString(value):
    if type(value) is unicode:
        value=value.replace("'","_")
        value=value.replace("\"","_")
    return value

#############################################################
#CONNECT TO DATABASE
#############################################################
DATABASE="MinorBodies"
USER="minorbodies"
PASSWORD="347940"
con=mdb.connect("localhost",USER,PASSWORD,DATABASE)
db=con.cursor()

#############################################################
#READ DATA
#############################################################
out=System("ls -m parts/*.json")
listf=out.split(",")
ff=open("failed.dat","w")
for jfile in listf:
    jfile=jfile.strip()
    print "Reading %s..."%jfile
    bodies=json.load(open(jfile))
    for body in bodies:
        #print "\tReading object %s..."%body["Principal_desig"]
        sql="insert into Bodies "
        fieldst="("
        values="("
        fvalues=""
        fields=body.keys()
        for field in fields:
            fieldst+="%s,"%field
            value=body[field]
            if type(value) is list:
                value=",".join(value)
            value=replaceString(value)
            values+="'%s',"%value
            fvalues+="%s = '%s',"%(field,value)
        fieldst=fieldst.strip(",")+")"
        values=values.strip(",")+")"
        fvalues=fvalues.strip(",")
        sql+="%s values %s on duplicate key update %s"%(fieldst,values,fvalues)
        #print sql
        try:
            db.execute(sql)
            con.commit()
        except:
            ff.write("jfile=%s\n"%jfile)
            ff.write("body=%s\n\n"%body["Principal_desig"])
            ff.write("error=\n%s"%sys.exc_info()[0])
            ff.write("\n")
ff.close()
