import sys

from models import app, db, Venue, Artist, Show
from forms import *
from flask import render_template, request

#  Venue
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
  data = []
  cities = Venue.query.with_entities(Venue.city, Venue.state).group_by(Venue.city, Venue.state).all()

  for city in cities:
    venues_data = []
    venues =  Venue.query.filter_by(state=city.state).filter_by(city=city.city).all()
    for venue in venues:
      venues_data.append({
        "id": venue.id,
        "name": venue.name,
        "num_upcoming_shows": len(db.session.query(Show).filter(Show.venue_id==venue.id).filter(Show.start_time>datetime.now()).all())
      })
    data.append({
      "city": city.city,
      "state": city.state,
      "venues": venues_data
    })

  return render_template('pages/venues.html', areas=data)

@app.route('/venues/search', methods=['POST'])
def search_venues():
  # seach for Hop should return "The Musical Hop".
  # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"
  search_term = request.form.get('search_term', '')
  search_results = db.session.query(Venue).filter(Venue.name.ilike(f'%{search_term}%')).all()
  data = []

  for search in search_results:
    data.append({
      "id": search.id,
      "name": search.name,
      "num_upcoming_shows": len(db.session.query(Show).filter(Show.venue_id==search.id).filter(Show.start_time>datetime.now()).all())
    })
  response={
    "count": len(search_results),
    "data": data
  }
  return render_template('pages/search_venues.html', results=response, search_term=search_term)

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  # shows the venue page with the given venue_id
  venue = Venue.query.get(venue_id)
  shows = Show.query.join(Artist).filter(Show.venue_id==venue_id).all()
  past_shows = []
  upcoming_shows = []
  for show in shows:
    show_detail = {
      "artist_id": show.artist_id,
      "artist_name": show.artist.name,
      "artist_image_link": show.artist.image_link,
      "start_time": show.start_time.strftime('%Y-%m-%d %H:%M:%S')
    }
    if show.start_time<datetime.now():
      past_shows.append(show_detail)
    else:
      upcoming_shows.append(show_detail)
  data = {
    "id": venue.id,
    "name": venue.name,
    "genres": venue.genres,
    "address": venue.address,
    "city": venue.city,
    "state": venue.state,
    "phone": venue.phone,
    "website": venue.website_link,
    "facebook_link": venue.facebook_link,
    "seeking_talent": venue.seeking_talent,
    "seeking_description": venue.seeking_description,
    "image_link": venue.image_link,
    "past_shows": past_shows,
    "upcoming_shows": upcoming_shows,
    "past_shows_count": len(past_shows),
    "upcoming_shows_count": len(upcoming_shows),
  }
  return render_template('pages/show_venue.html', venue=data)

#  Artist
#  ----------------------------------------------------------------

@app.route('/artists')
def artists():
  data = []
  artists = Artist.query.all()
  for artist in artists:
    data.append({
      "id": artist.id,
      "name": artist.name
    })
  return render_template('pages/artists.html', artists=data)

@app.route('/artists/search', methods=['POST'])
def search_artists():
  # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
  # search for "band" should return "The Wild Sax Band".
  search_term = request.form.get('search_term', '')
  search_results = db.session.query(Artist).filter(Artist.name.ilike(f'%{search_term}%')).all()
  data = []

  for search in search_results:
    data.append({
      "id": search.id,
      "name": search.name,
      "num_upcoming_shows": len(db.session.query(Show).filter(Show.artist_id==search.id).filter(Show.start_time>datetime.now()).all())
    })
  response={
    "count": len(search_results),
    "data": data
  }
  return render_template('pages/search_artists.html', results=response, search_term=search_term)

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  # shows the artist page with the given artist_id
  artist = Artist.query.get(artist_id)
  shows = Show.query.join(Venue).filter(Show.artist_id==artist_id).all()
  past_shows = []
  upcoming_shows = []
  for show in shows:
    show_detail = {
      "venue_id": show.venue_id,
      "venue_name": show.venue.name,
      "venue_image_link": show.venue.image_link,
      "start_time": show.start_time.strftime('%Y-%m-%d %H:%M:%S')
    }
    if show.start_time<datetime.now():
      past_shows.append(show_detail)
    else:
      upcoming_shows.append(show_detail)
  data = {
    "id": artist.id,
    "name": artist.name,
    "genres": artist.genres,
    "city": artist.city,
    "state": artist.state,
    "phone": artist.phone,
    "website": artist.website_link,
    "facebook_link": artist.facebook_link,
    "seeking_venue": artist.seeking_venue,
    "seeking_description": artist.seeking_description,
    "image_link": artist.image_link,
    "past_shows": past_shows,
    "upcoming_shows": upcoming_shows,
    "past_shows_count": len(past_shows),
    "upcoming_shows_count": len(upcoming_shows),
  }
  return render_template('pages/show_artist.html', artist=data)

#  Show
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  # displays list of shows at /shows
  data = []
  shows = Show.query.join(Artist).join(Venue).all()
  for show in shows:
    data.append({
      "venue_id": show.venue_id,
      "venue_name": show.venue.name,
      "artist_id": show.artist_id,
      "artist_name": show.artist.name,
      "artist_image_link": show.artist.image_link,
      "start_time": show.start_time.strftime('%Y-%m-%d %H:%M:%S')
    })
  return render_template('pages/shows.html', shows=data)