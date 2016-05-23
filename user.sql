create user 'minorbodies'@'localhost' identified by '347940';
create database MinorBodies;
grant all privileges on MinorBodies.* to 'minorbodies'@'localhost';
flush privileges;
