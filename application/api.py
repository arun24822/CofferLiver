from sqlalchemy import Column, Integer, String, Float
from application import app,db,marsh

@app.cli.command('db_create')
def db_create():
    db.create_all()
    print("database created")


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database deleted')


@app.cli.command('db_seed')
def db_seed():
    test_user = User(
        first_name = 'Arun',
        last_name = 'Kumar',
        email = 'arun2822@gmail.com',
        password = 'arun24822' 
    )

    db.session.add(test_user)
    db.session.commit()#to save.
    print('Database Seeded')

#we cannot serialise planet db data into json
#database models
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    

class BasicHepatitis(db.Model):
    __tablename__ = 'basic_hepatitis'
    pateint_id = Column(Integer, primary_key=True)
    age = Column(Integer)
    sex = Column(String)
    alb = Column(Float)
    alp = Column(Float)
    alt = Column(Float)
    ast = Column(Float)
    bil = Column(Float)
    che = Column(Float)
    chol = Column(Float)
    crea = Column(Float)
    ggt = Column(Float)
    prot = Column(Float)
    category = Column(String)


#for serialization
class UserSchema(marsh.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password')

class PlanetSchema(marsh.Schema):
    class Meta:
        fields = ('planet_id', 'planet_name', 'planet_type', 'home_star', 'mass', 'radius', 'distance')


#instatiate 2 diff schema object for both schemas

user_schema = UserSchema()#for getting one record
users_schema = UserSchema(many = True)#for getting many records from the data base.

planet_schema = PlanetSchema()
planets_schema = PlanetSchema(many = True)