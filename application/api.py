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
    mercury = Planet(
        planet_name = 'Mercury',
        planet_type = 'Class D',
        home_star = 'Sol',
        mass = 3.258e23,
        radius = 1516,
        distance = 35.98e6
    )
    venus = Planet(
        planet_name = 'Venus',
        planet_type = 'Class K',
        home_star = 'Sol',
        mass = 4.867e24,
        radius = 3760,
        distance = 67.24e6
    )
    earth = Planet(
        planet_name = 'Earth',
        planet_type = 'Class M',
        home_star = 'Sol',
        mass = 5.927e24,
        radius = 3959,
        distance = 92.96e6
    )

    db.session.add(mercury)
    db.session.add(venus)
    db.session.add(earth)


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


class Planet(db.Model):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    planet_type = Column(String)
    home_star = Column(String)
    mass = Column(Float)
    radius = Column(Float)
    distance = Column(Float)


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