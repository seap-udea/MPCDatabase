from mpcdb import *

results=mysqlSelect(selection="max(a)")
print "The minor body with maximum a is:",results[0]["max(a)"]

results=mysqlSelect(selection="Name,Principal_desig",condition="where NEO_flag<>0 or PHA_flag<>0")
print "The number of NEOs and PHAs now is",len(results)

results=mysqlSelect(selection="Name,a",condition="order by a desc limit 10")
print results

print "This is the information about (347940) Jorgezuluaga:"
results=mysqlSelect(condition="where Name like '%zuluaga%'")

for key in results[0].keys():
    print key,":",results[0][key],",",

