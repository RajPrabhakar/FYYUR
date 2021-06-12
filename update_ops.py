import sys

from models import app, db, Venue, Artist
from forms import *
from flask import render_template, request, flash, redirect, url_for

#  Venue
#  ----------------------------------------------------------------

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  venue = Venue.query.get(venue_id)
  form = VenueForm(obj=venue)
  return render_template('forms/edit_venue.html', form=form, venue=venue)

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  # venue record with ID <venue_id> using the new attributes
  form = VenueForm(request.form)
  error = False
  try:
    venue = Venue.query.get(venue_id)
    form.populate_obj(venue)
    db.session.commit()
  except:
    error = True
    db.session.rollback()
    print(sys.exc_info())
  finally:
    db.session.close()

  if not error:
    flash('Venue ' + request.form['name'] + ' was successfully updated!')
  else:
    flash('Uh-Oh')
  return redirect(url_for('show_venue', venue_id=venue_id))

#  Artist
#  ----------------------------------------------------------------

@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  artist = Artist.query.get(artist_id)
  form = ArtistForm(obj=artist)
  return render_template('forms/edit_artist.html', form=form, artist=artist)

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  # artist record with ID <artist_id> using the new attributes
  form = ArtistForm(request.form)
  error = False
  try:
    artist = Artist.query.get(artist_id)
    form.populate_obj(artist)
    db.session.commit()
  except:
    error = True
    db.session.rollback()
    print(sys.exc_info())
  finally:
    db.session.close()

  if not error:
    flash('Artist ' + request.form['name'] + ' was successfully updated!')
  else:
    flash('Uh-Oh')

  return redirect(url_for('show_artist', artist_id=artist_id))

#  Show
#  ----------------------------------------------------------------