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

