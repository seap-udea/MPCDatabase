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

