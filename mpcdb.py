###################################################
#EXTERNAL PACKAGES
###################################################
import MySQLdb as mdb
from sys import argv,exit

###################################################
#CONFIGURATION
###################################################
DATABASE="MinorBodies"
USER="minorbodies"
PASSWORD="347940"
CON=mdb.connect("localhost",USER,PASSWORD,DATABASE)
DB=CON.cursor()

###################################################
#ROUTINES
###################################################
class dict2obj(object):
    def __init__(self,dic={}):self.__dict__.update(dic)
    def __add__(self,other):
        for attr in other.__dict__.keys():
            exec("self.%s=other.%s"%(attr,attr))
        return self

def mysqlSelect(selection="*",table="Bodies",condition=""):

    #QUERY
    sql="select %s from %s %s"%(selection,table,condition)
    DB.execute(sql)
    results=DB.fetchall()

    if selection=="*":
        #RECOVER ALL COLUMNS IN TABLE
        DB.execute("show columns from %s"%table)
        fields=DB.fetchall()
    else:
        #ONLY COLUMNS IN SELECTION
        fields=[(field,) for field in selection.split(",")]

    dresults=[]
    for result in results:
        row=dict()
        for i in xrange(len(fields)):
            field=fields[i][0]
            row[field]=result[i]
        dresults+=[row]
    return dresults
    
