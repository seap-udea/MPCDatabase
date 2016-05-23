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
	@echo "Restoring database MinorBodies..."
	@cat data/MinorBodies.sql.7z-* > data/MinorBodies.sql.7z
	@p7zip -d data/MinorBodies.sql.7z
	@echo "Installing MinorBodies data into MySQL server..."
	@echo "Enter root MySQL password..."
	@mysql -u root -p MinorBodies < data/MinorBodies.sql
	@rm data/MinorBodies.sql

install:
	@echo "Creating user and database..."
	@echo "You need to provide several times the root password of MySQL server:"
	@mysql -u root -p < user.sql
	@echo "User and database created..."
	@make restore
