from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions
class UserProfile(db.Model):
    __tablename__ = 'user_profile'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    facebook_id = db.Column(db.String(64), nullable=False, unique=True)
    first_name = db.Column(db.String(64), nullable=True)
    last_name = db.Column(db.String(64), nullable=True)
    email = db.Column(db.String(64), nullable=True)

class PictureLikes(db.model):
    __tablename__ = 'pictures'
    id = db.Column(db.Integer, primary_key=True)
    likes = db.Column(db.Integer, nullable=True)


##############################################################################
# Helper Functions
def seed_data():
    """ Fill database with sample data to start with """

    # Pictures
    pic1 = User(id=1, likes=0)
    pic2 = User(id=2, likes=0)
    pic3 = User(id=3, likes=0)
    pic4 = User(id=4, likes=0)
    pic5 = User(id=5, likes=0)
    pic6 = User(id=6, likes=0)
    pic7 = User(id=7, likes=0)
    pic8 = User(id=8, likes=0)
    pic9 = User(id=9, likes=0)
    pic10 = User(id=10, likes=0)
    pic11 = User(id=11, likes=0)
    pic12 = User(id=12, likes=0)
    pic13 = User(id=13, likes=0)
    pic14 = User(id=14, likes=0)
    pic15 = User(id=15, likes=0)
    pic16 = User(id=16, likes=0)
    pic17 = User(id=17, likes=0)
    pic18 = User(id=18, likes=0)
    pic19 = User(id=19, likes=0)
    pic20 = User(id=20, likes=0)
    pic21 = User(id=21, likes=0)
    pic22 = User(id=22, likes=0)
    pic23 = User(id=23, likes=0)

    db.session.add_all([pic1, pic2, pic3, pic4, pic5, pic6, pic7, pic8, pic9, pic10, pic11, pic12, pic13, pic14, pic15, pic16, pic17, pic18, pic19, pic20, pic21, pic22, pic23])
    db.session.commit()

def connect_to_db(app, psql_server):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = psql_server
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)



if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app, 'postgresql:///h4hproject')
    seed_data()
    print "Connected to DB."
    db.create_all()