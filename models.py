#!/usr/bin/env python
#-*-coding:UTF-8-*-

from peewee import *
from settings import *
import datetime

db = MySQLDatabase(MYSQL_DB, user=MYSQL_USER,passwd=MYSQL_PASSWORD)

class BaseModel(Model):
    created_date = DateTimeField(default=datetime.datetime.now)
    del_flag = BooleanField(default=False)
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique = True)
    password = CharField()
    gender = BooleanField()
    token = CharField(unique = True)
    last_date = DateTimeField(default=datetime.datetime.now)
    

    def __unicode__(self):
        return 'id:%-4dusername:%s'%(self.id,self.username)

    @classmethod
    def create(self,**argv):
        import hashlib
    	argv['token'] = hashlib.sha224(argv['username']).hexdigest()
    	return super(User,self).create(**argv)

    @staticmethod
    def create_token(str):
		import hashlib
		return hashlib.sha224(str).hexdigest()

    def update_last_date(self):
        now = datetime.datetime.now()
        self.last_date = now
        self.save()



class Activity(BaseModel):
    user = ForeignKeyField(User,related_name='activities_host')
    pic = CharField()
    title = CharField()
    content = CharField()
    activity_type = IntegerField()
    duaration = IntegerField()
    close_flag = BooleanField(default = False)


    def __unicode__(self):
        return 'user:%s   title:%s'%(self.user,self.title)

class Picture(BaseModel):
    activity = ForeignKeyField(Activity,related_name='pics')
    pic_url = CharField()

    def __unicode__(self):
        return self.pic_url

class Activity_Participant(BaseModel):
    user = ForeignKeyField(User,related_name='activities_participated')
    activity = ForeignKeyField(Activity,related_name='participants')

class Message(BaseModel):
    user_from = ForeignKeyField(User,related_name='messages_from')
    user_to = ForeignKeyField(User,related_name='messages_to')
    content = CharField()



if __name__ == '__main__':
    db.connect()
    #Activity.drop_table()
    #User.create_table()
    #Activity.create_table()
    #Picture.create_table()
    #Message.create_table()
    #user = User.get()
    #Activity.create(user=user,title='cc').save()
    #User.select().where(User.id == 1)
    #print Activity.select().where(Activity.user==1).get()
    #for activitiy in user.activities.offset(0).limit(1).order_by(Activity.id.desc()):
    #    print activitiy
    for i in range(300,1000000):
        aa = str(i)
        user = User.create(username=aa,password='222',gender=True)
