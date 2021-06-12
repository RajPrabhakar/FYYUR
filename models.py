from app import db

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
  __tablename__ = 'venue'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  city = db.Column(db.String(120), nullable=False)
  state = db.Column(db.String(120), nullable=False)
  address = db.Column(db.String(120), nullable=False)
  phone = db.Column(db.String(120), nullable=False)
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))

  # TODO: implement any missing fields, as a database migration using Flask-Migrate

  genres = db.Column(db.ARRAY(db.String()))
  website_link = db.Column(db.String(120))
  looking_for_talent = db.Column(db.Boolean, nullable=False, default=False)
  description = db.Column(db.String(240))
  show = db.relationship('Show', backref='venue', lazy=True)

  def __repr__(self):
    return f'<Venue {self.id} : {self.name}>'

class Artist(db.Model):
  __tablename__ = 'artist'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  city = db.Column(db.String(120))
  state = db.Column(db.String(120))
  phone = db.Column(db.String(120), nullable=False)
  genres = db.Column(db.ARRAY(db.String()), nullable=False)
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))

  # TODO: implement any missing fields, as a database migration using Flask-Migrate

  website_link = db.Column(db.String(120))
  looking_for_venues = db.Column(db.Boolean, nullable=False, default=False)
  description = db.Column(db.String(240))
  show = db.relationship('Show', backref='artist', lazy=True)

  def __repr__(self):
    return f'<Artist {self.id} : {self.name}>'

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

class Show(db.Model):
  __tablename__ = 'show'

  id = db.Column(db.Integer, primary_key=True)
  artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
  venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
  start_time = db.Column(db.DateTime, nullable=False)

  def __repr__(self):
    return f'<Show {self.id} : {self.artist_id} : {self.venue_id}>'