#!/bin/bash
DBUSER="minorbodies"
DBPASSWORD="347940"
filename="MinorBodies"

echo "Dumping..."
mysqldump -u $DBUSER --password="$DBPASSWORD" MinorBodies > data/$filename.sql
echo "Compressing..."
p7zip data/$filename.sql
echo "Splitting..."
cd data/
rm $filename.sql.7z-*
split -b 1024k $filename.sql.7z $filename.sql.7z-
echo "Git adding..."
rm $filename.sql.7z
git add *
cd - &> /dev/null
echo "Done."
