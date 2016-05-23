clean:
	@find . -name "*~" -exec rm -rf {} \;
	@find . -name "#" -exec rm -rf {} \;
	@rm -rf *.pyc

commit:
	@echo "Commiting..."
	@-git commit -am "Commit"
	@-git push origin master

pull:
	@-git reset --hard HEAD
	@-git pull

backup:
	@echo "Backuping database..."
	@bash backup.sh

restore:
	@echo "Restoring table Quakes..."
	@cat data/MinorBodies.sql.7z-* > data/MinorBodies.sql.7z
	@p7zip -d data/MinorBodies.sql.7z
	@echo "Enter root mysql password..."
	@mysql -u root -p MinorBodies < data/MinorBodies.sql
	@p7zip data/MinorBodies.sql
