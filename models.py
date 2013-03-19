#!/usr/bin/env python
#-*-coding:UTF-8-*-

import peewee
from settings import *
import datetime

db = peewee.MySQLDatabase(MYSQL_DB, user=MYSQL_USER,passwd=MYSQL_PASSWORD)

class BaseModel(peewee.Model):
    class Meta:
        database = db

class User(BaseModel):
    username = peewee.CharField(unique = True)
    password = peewee.CharField()
    gender = peewee.BooleanField()
    token = peewee.CharField(unique = True)
    last_date = peewee.DateTimeField(default=datetime.datetime.now)
    created_date = peewee.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.username

    @staticmethod
    def create(**argv):
    	argv['token'] = User.create_token(argv['username'])
    	return User(**argv)

    @staticmethod
    def create_token(str):
		import hashlib
		return hashlib.sha224(str).hexdigest()


if __name__ == '__main__':
	db.connect()
	User.drop_table()
	User.create_table()
	#User.create(username="hou1",password="aa").save()
	#User.create_table()