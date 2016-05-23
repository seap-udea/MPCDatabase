#!/usr/bin/env python
import json,gzip,re

f=gzip.open("mpcorb_extended.json.gz", "rb")
size=500
block="["
iblock=1
nblock=1
for line in f:
    line=line.strip()
    if line=='[':continue
    if line==']':continue
    if not re.match("},",line):
        block+=line+"\n"
    else:
        block+="},"
        iblock+=1
        if (iblock%size)==0:
            print "Storing block %d..."%(nblock)
            block=block.strip(",")+"]"
            fblock=open("parts/mpcorb-%06d.json"%nblock,"w")
            fblock.write(block)
            fblock.close()
            nblock+=1
            iblock=1
            block="["


if iblock>1:
    print "Storing block %d..."%(nblock)
    block=block.strip(",")+"]"
    fblock=open("parts/mpcorb-%06d.json"%nblock,"w")
    fblock.write(block)
    fblock.close()

