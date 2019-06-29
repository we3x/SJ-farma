from mongoengine import *
import hashlib

class User(Document):
    password = StringField(max_length=128)
    first_name = StringField(max_length=32)
    last_name = StringField(max_length=32)
    email = StringField(max_length=64)

    meta = {
        'allow_inheritance': True,
        'indexes': [
            {'fields': ['email'], 'unique': True}
        ]
    }

    def __unicode__(self):
        return "User: "+self.email

    def check_password(self, raw_password):
        hash_password = hashlib.sha256(raw_password.encode('utf-8')).hexdigest()
        return self.password == hash_password

    def save_user(self):
        self.password = hashlib.sha256(self.password.encode('utf-8')).hexdigest()
        self.save()

    @staticmethod
    def auth(email, password):
        user = User.objects.get(email=email)
        if user.check_password(password):
            return user
        else:
            raise Exception("Invalid passowrd")

