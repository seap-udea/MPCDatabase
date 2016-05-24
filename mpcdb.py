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
    DB.execute("show columns from %s"%table)
    fields=DB.fetchall()
    
    sql="select %s from %s %s"%(selection,table,condition)
    DB.execute(sql)
    results=DB.fetchall()

    if selection!="*":
        fields=[(field,) for field in selection.split(",")]

    dresults=[]
    for result in results:
        row=dict()
        for i in xrange(len(fields)):
            field=fields[i][0]
            row[field]=result[i]
        dresults+=[row]
    return dresults
    
def loadDatabase(server='localhost',
                 user=USER,
                 password=PASSWORD,
                 database=DATABASE):
    con=mdb.connect(server,user,password,database)
    with con:
        dbdict=dict()
        db=con.cursor()
        db.execute("show tables;")
        tables=db.fetchall()
        for table in tables:
            table=table[0]
            dbdict[table]=dict()
            
            db.execute("show columns from %s;"%table)
            fields=db.fetchall()
            dbdict[table]['fields']=[]
            for field in fields:
                fieldname=field[0]
                fieldtype=field[3]
                dbdict[table]['fields']+=[fieldname]
                if fieldtype=='PRI':
                    dbdict[table]['primary']=fieldname

            db.execute("select * from %s;"%table)
            rows=db.fetchall()

            dbdict[table]['rows']=dict()
            for row in rows:
                rowdict=dict()
                i=0
                for field in dbdict[table]['fields']:
                    rowdict[field]=row[i]
                    if field==dbdict[table]['primary']:
                        primary=str(row[i]).strip()
                    i+=1
                dbdict[table]['rows'][primary]=rowdict

    return dbdict,con

